import numpy as np
import plotly.graph_objects as go

# Funkcija za simulaciju temperature
def simulacija_temp_plotly(mean, std_dev, broj_mjerenja=24):
    np.random.seed(0)
    temperature = np.random.normal(loc=mean, scale=std_dev, size=broj_mjerenja)
    promjene = np.diff(temperature)

    print(f"\n--- Simulacija (mean={mean}, std={std_dev}) ---")
    print("Temperature:", np.round(temperature, 2))
    print("Promjene (razlike):", np.round(promjene, 2))
    print("Prosječna apsolutna promjena:", round(np.mean(np.abs(promjene)), 2))

    # Kreiranje grafova pomoću Plotly
    fig = go.Figure()

    # Temperatura po satu
    fig.add_trace(go.Scatter(
        x=list(range(broj_mjerenja)),
        y=temperature,
        mode='lines+markers',
        name='Temperatura',
        line=dict(color='blue')
    ))

    # Promjene između sati (diff)
    fig.add_trace(go.Scatter(
        x=list(range(1, broj_mjerenja)),
        y=promjene,
        mode='lines+markers',
        name='Promjene',
        line=dict(color='red')
    ))

    # Prikaz grafa
    fig.update_layout(
        title=f"Simulacija temperature (Mean={mean}, StdDev={std_dev})",
        xaxis_title="Sat",
        yaxis_title="°C / Promjena",
        legend=dict(x=0, y=1),
        template="plotly_white"
    )

    fig.show()

#  Pokretanje simulacije sa različitim parametrima
simulacija_temp_plotly(mean=20, std_dev=1)
simulacija_temp_plotly(mean=20, std_dev=5)
simulacija_temp_plotly(mean=30, std_dev=2)