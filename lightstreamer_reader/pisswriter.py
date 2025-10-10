import time
import pandas as pd
from datetime import datetime
from pathlib import Path
from .pissstream import generate_continuous_fetcher


# Caminho absoluto relativo à pasta ISS_PISSTANK
def ensure_data_dir() -> Path:
    # Caminho absoluto relativo à pasta ISS_PISSTANK
    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(exist_ok=True)
    return data_dir / "urine_log.csv"

#Cria uma linha com timestamp e valor
def create_entry(value: int) -> pd.DataFrame:
    return pd.DataFrame([{
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "capacity_percent": value
    }])
#Salva a entrada no CSV (cria ou anexa)
def save_entry(df: pd.DataFrame, csv_path: Path):
    df.to_csv(csv_path, mode="a", header=not csv_path.exists(), index=False)
    
#Executa o loop de captura e gravação.    
def run_capture_loop(fetcher, csv_path: Path, poll_interval=2.0, skip_duplicates=True):
    print(f"Iniciando captura contínua. Salvando em {csv_path} ...")

    last_value = None
    while True:
        try:
            value = fetcher()
            if not skip_duplicates or value != last_value:
                df = create_entry(value)
                save_entry(df, csv_path)
                print(f"{datetime.now().strftime('%H:%M:%S')} - {value}%")
                last_value = value
            time.sleep(poll_interval)
        except KeyboardInterrupt:
            print("\nCaptura interrompida pelo usuário.")
            break

def main():
    csv_path = ensure_data_dir()  
    fetcher = generate_continuous_fetcher()
    run_capture_loop(fetcher, csv_path)
