import nidaqmx  # Biblioteca para aquisição de dados NI-DAQmx
import matplotlib.pyplot as plt  # Para plotar gráficos

# Configuração do dispositivo DAQ
device_name = "Dev1"  # Nome do dispositivo DAQ (altere conforme necessário)
temp_channel = "ai0"  # Canal de entrada analógica para temperatura (altere conforme necessário)
heat_channel = "ai1"  # Canal de entrada analógica para fluxo de calor (altere conforme necessário)
sample_rate = 1000.0  # Taxa de amostragem em Hz
num_samples = 1000  # Número de amostras a serem adquiridas

# Configuração dos gráficos
plt.ion()  # Modo de interatividade para atualização contínua dos gráficos
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.set_title("Aquisição de Dados de Temperatura")
ax1.set_ylabel("Temperatura (°C)")
ax2.set_title("Aquisição de Dados de Transferência de Calor")
ax2.set_ylabel("Transferência de Calor (W)")
ax2.set_xlabel("Tempo (s)")
ax1.grid(True)
ax2.grid(True)

# Inicialização dos objetos de tarefa DAQ
with nidaqmx.Task() as temp_task, nidaqmx.Task() as heat_task:
    temp_task.ai_channels.add_ai_voltage_chan(f"{device_name}/{temp_channel}")  # Configuração do canal de temperatura
    heat_task.ai_channels.add_ai_voltage_chan(f"{device_name}/{heat_channel}")  # Configuração do canal de fluxo de calor
    temp_task.timing.cfg_samp_clk_timing(rate=sample_rate, samps_per_chan=num_samples)  # Configuração da taxa de amostragem
    heat_task.timing.cfg_samp_clk_timing(rate=sample_rate, samps_per_chan=num_samples)  # Configuração da taxa de amostragem

    # Aquisição de dados
    temperature_data = temp_task.read(number_of_samples_per_channel=num_samples)
    heat_data = heat_task.read(number_of_samples_per_channel=num_samples)
    time_data = [i / sample_rate for i in range(num_samples)]

    # Plotagem dos dados
    ax1.plot(time_data, temperature_data, 'b-')
    ax2.plot(time_data, heat_data, 'r-')
    plt.draw()

# Mantenha a janela dos gráficos aberta até que você a feche manualmente
plt.show(block=True)
