import streamlit as sl

sl.title("CALCULADORA DE SUBSTITUIÇÃO TRIBUTÁRIA DO ICMS")
sl.subheader("Simplificando o cálculo do ICMS-ST.")

estados_brasileiros = ("Escolha um estado","Acre", "Alagoas", "Amapá", "Bahia", "Espírito Santo", "Maranhão",
    "Mato Grosso", "Mato Grosso do Sul","Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro",
    "Rio Grande do Norte", "Rio Grande do Sul","Sergipe", "Tocantins")

# ESTADO - ALIQUOTA - REDUÇÃO - FCP - ALIQUOTA

estados_mva_aliquota = {"Pernambuco":[[1.4134,20.50],[1.4134,20.50],[0,0,20.50]],"Acre":[[1.6753,4],[1.5357,12],[0,0,19]],
                        "Bahia":[[1.7072,4],[1.5650,12],[0,0,20.50]],"Espírito Santo":[[1.6348,4],[1.4985,12],[0,0,17]],
                        "Maranhão":[[1.7396,4],[1.5946,12],[0,0,22]],"Mato Grosso":[[1.4605,4],[1.4605,12],[0,0,17]],
                        "Paraíba":[[1.6661,4],[1.5547,12],[0,0,20]],"Piauí":[[1.7180,4],[1.5749,12],[0,0,21]],
                        "Rio Grande do Sul":[[1.9153,4], [1.7557,12],[0,0,17]],"Amapá":[[1.6552,4],[1.5173,12],[10,0,18]],
                        "Rio Grande do Norte":[[1.6961,4],[1.5547,12],[10,0,18]],"Sergipe":[[1.6966,4],[1.5512,12],[0,1,21]],
                        "Pará":[[1.6751,4],[1.5355,12],[36.84,0,19]],"Alagoas":[[1.6751,4],[1.5355,12],[0,1,20]],
                        "Tocantins":[[1.6961,4],[1.5547,12],[0,0,20]],"Rio de Janeiro":[[1.6970,4],[1.5556,12],[0,2,22]],
                        "Mato Grosso do Sul":[[1.4713,4],[1.4713,12],[0,0,17]]}

nacionalidade = ("Escolha a nacionalidade","Importado","Nacional")




def icms_st():
        for i,y in estados_mva_aliquota.items():
            if i == select_estado and select_nacionalidade == "Importado":
                        valor_descontoparacalculo= float(valor)*(float(desconto)/100)
                        valor_desconto = f"R$ {(float(valor) * (float(desconto)/100)):.2f}"
                        totalRs = float(valor)-valor_descontoparacalculo+int(frete)
                        mva = totalRs * (y[0][0]-1)
                        baseparacalculo=totalRs+mva-(totalRs+mva)*y[2][0]/100
                        basecalculo = f"R$ {totalRs+mva:.2f}"
                        icmsst = baseparacalculo*(y[2][2]/100)
                        creditoicms= totalRs*(y[0][1]/100)
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
                        mva = totalRs * (y[1][0]-1)
                        baseparacalculo=totalRs+mva-(totalRs+mva)*y[2][0]/100
                        basecalculo = f"R$ {totalRs+mva:.2f}"
                        icmsst = baseparacalculo*(y[2][2]/100)
                        creditoicms= totalRs*(y[1][1]/100)
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