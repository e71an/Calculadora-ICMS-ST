import streamlit as sl

sl.title("CALCULADORA DE SUBSTITUIÇÃO TRIBUTÁRIA DO ICMS")
sl.subheader("Simplificando o cálculo do ICMS-ST.")

estados_brasileiros = ("Escolha um estado","Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará",
    "Distrito Federal", "Espírito Santo", "Goiás", "Maranhão",
    "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará",
    "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro",
    "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia",
    "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins")


estados_mva_aliquota = {"Pernambuco":[1.4134,1.4134,20.50],"Bahia":[1.7072,1.5650,20.50],"Espírito Santo":[1.6348,1.4985,17],
                        "Maranhão":[1.7396,1.5946,22],"Mato Grosso":[1.6035,1.6035,17],"Paraíba":[1.6661,1.5547,20],
                        "Paraná":[1.6860,1.5455,19.50],"Rio Grande do Sul":[1.9153, 1.7557,17],"Amapá":[1.6552,1.5173,18],
                        "Rio Grande do Norte":[1.6961,1.5547,18,10],"Sergipe":[1.6966,1.5512,20,0.01],
                        "Pará":[0.6751,0.5355,19,0.3684],"Alagoas":[1.6751,1.5355,19,0.01],"Tocantins":[1.6961,1.5547,20],
                        "Rio de Janeiro":[1.6970,1.5556,20,0.02]}

nacionalidade = ("Escolha a nacionalidade","Importado","Nacional")




def icms_st():
        for i,y in estados_mva_aliquota.items():
            if i == select_estado and select_nacionalidade == "Importado":
                        valor_descontoparacalculo= float(valor) * (float(desconto)/100)
                        valor_desconto = f"R$ {(float(valor) * (float(desconto)/100)):.2f}"
                        totalRs = float(valor)-valor_descontoparacalculo+int(frete)
                        mva = totalRs * (y[0]-1)
                        baseparacalculo=totalRs+mva
                        basecalculo = f"R$ {totalRs+mva:.2f}"
                        icmsst = baseparacalculo*(y[2]/100)
                        creditoicms= totalRs*0.04
                        valotsr = f"R$ {icmsst-creditoicms:.2f}"
                        valotsrparacalculo = icmsst-creditoicms
                        totalacobra = f"R$ {valotsrparacalculo+totalRs:.2f}"                       
                        sl.metric(label= "Valor do Desconto: ", value=valor_desconto)
                        sl.metric(label= "Base de Calculo: ", value=basecalculo)
                        sl.metric(label= "Valor ICMS-ST: ", value=valotsr)
                        sl.metric(label= "Total à cobra: ", value=totalacobra)

            elif i == select_estado and select_nacionalidade == "Nacional" :
                        valor_descontoparacalculo= float(valor) * (float(desconto)/100)
                        valor_desconto = f"R$ {(float(valor) * (float(desconto)/100)):.2f}"
                        totalRs = float(valor)-valor_descontoparacalculo+int(frete)
                        mva = totalRs * (y[1]-1)
                        baseparacalculo=totalRs+mva
                        basecalculo = f"R$ {totalRs+mva:.2f}"
                        icmsst = baseparacalculo*(y[2]/100)
                        creditoicms= totalRs*0.12
                        valotsr = f"R$ {icmsst-creditoicms:.2f}"
                        valotsrparacalculo = icmsst-creditoicms
                        totalacobra = f"R$ {valotsrparacalculo+totalRs:.2f}"                       
                        sl.metric(label= "Valor do Desconto: ", value=valor_desconto)
                        sl.metric(label= "Base de Calculo: ", value=basecalculo)
                        sl.metric(label= "Valor ICMS-ST: ", value=valotsr)
                        sl.metric(label= "Total à cobra: ", value=totalacobra)


valor = sl.text_input("Digite o valor dos produtos:", key="n1")
desconto = sl.text_input("Digite percentual de desconto:", key="n2")
frete = sl.text_input("Digite o valor do frete:", key="n3")

select_estado = sl.selectbox("Qual estado destinatario? Selecione", key='estado', options = estados_brasileiros)
select_nacionalidade = sl.selectbox("Qual a nacionalidade do produto? Selecione", key='nacionalidade', options = nacionalidade)

icms_st()