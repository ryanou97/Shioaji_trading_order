# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 16:21:38 2023

@author: smile
"""

import shioaji as sj
import accountInfo



api = sj.Shioaji(simulation=True) # 模擬模式
accounts = api.login(
    api_key = accountInfo.my_api_key,     # 請修改此處
    secret_key = accountInfo.my_secret_key,   # 請修改此處
    contracts_cb = print
)



text = "BRF, BTF, CAF, CBF, CCF, CDF, CE1, CEF, CFF, CGF, CHF, CJF, CKF, CL1, CLF, CMF, CNF, CQF, CRF, CSF, CUF, CWF, CXF, CYF, CZF, DAF, DBF, DC1, DCF, DDF, DEF, DFF, DGF, DHF, DIF, DJF, DKF, DLF, DN1, DNF, DO1, DOF, DPF, DQ1, DQF, DSF, DVF, DWF, DXF, DYF, DZF, E4F, ECC, ECF, ECI, ECL, EEF, EGF, EHF, EKF, EMF, EPF, ESC, ESF, ESI, ESL, EXF, EYF, EZF, F1F, FBF, FCF, FE1, FEF, FFF, FGF, FKF, FN1, FNF, FQF, FRF, FTF, FVF, FWF, FXF, FYF, FZ1, FZF, G2F, GAF, GCF, GDF, GHF, GIF, GJF, GLF, GMF, GNF, GOF, GRF, GTF, GUF, GWF, GXF, GYF, GZF, HAF, HBF, HCF, HHF, HIF, HL1, HLF, HOF, HQF, HSF, IA1, IAF, IHF, IIF, IJF, IMF, IOF, IPF, IQF, IRF, ITF, IXF, IYF, IZF, JBF, JFF, JMF, JNF, JPF, JSF, JWF, JZF, KAF, KBF, KCF, KD1, KDF, KEF, KF1, KFF, KGF, KIF, KKF, KLF, KOF, KP1, KPF, KSF, KUF, KWF, LBF, LCF, LEF, LIF, LMF, LO1, LOF, LQF, LRF, LTF, LUF, LV1, LVF, LWF, LXF, LYF, MAF, MBF, MJF, MKF, MQF, MVF, MX1, MX4, MXF, MYF, NAF, NBF, NDF, NEF, NGF, NI1, NIF, NJF, NKC, NKF, NKI, NKL, NLF, NMF, NOF, NQF, NSF, NU1, NUF, NVF, NWF, NXF, NYF, OAF, OBF, OD1, ODF, OEF, OHF, OJF, OKF, OLF, OMF, OOF, OPF, OQF, ORF, OSF, OTF, OUF, OVF, OWF, OXF, OYF, OZF, PAF, PBF, PCF, PDF, PEF, PFF, PGF, PHF, PIF, PJF, PKF, PLF, PMF, PNF, PPF, PQF, PRF, PSF, PTF, PUF, PVF, PWF, PXF, PYF, PZF, QAF, QBF, QCF, QDF, QEF, QFF, QGF, QHF, QIF, QJF, QKF, QLF, QMF, QNF, QOF, QPF, QQF, QRF, QSF, QTF, QUF, QVF, QWF, QXF, QYF, QZF, RAF, RBF, RCF, RDF, REF, RFF, RGF, RHF, RIF, RJ1, RJF, RKF, RLF, RMF, RNF, RO1, ROF, RPF, RQF, RRF, RSF, RTF, RUF, RVF, RWF, RXF, RYF, RZF, SHF, SOF, SPF, TGF, TJF, TWN, TXF, UDF, UNF, XAF, XBF, XEF, XIF, XJF, YMC, YMF, YMI, YML, ZEF, ZFF"

# 使用split函数将文本分割成列表
code_list = text.split(", ")
count = text.count(',')



# 打印生成的列表
print(code_list)
print("count: ", count)




#  Shioaji_symbols_simple.txt

with open('symbols_simple.txt', 'w') as file:
    for i in range(count):
        symbole_code = code_list[i]
        print(code_list[i])
    
        if api.Contracts.Futures[code_list[i]][code_list[i] + '202312'] != None:
            txt_symbol = str(api.Contracts.Futures[code_list[i]][code_list[i] + '202312'].symbol)
            txt_name = str(api.Contracts.Futures[code_list[i]][code_list[i] + '202312'].name)
            print(txt_symbol)
            print(txt_name)
            
        elif api.Contracts.Futures[code_list[i]][code_list[i] + '202311'] != None:    
            txt_symbol = str(api.Contracts.Futures[code_list[i]][code_list[i] + '202311'].symbol)
            txt_name = str(api.Contracts.Futures[code_list[i]][code_list[i] + '202311'].name)
            print(txt_symbol)
            print(txt_name)
        
        else:
            txt_symbol = str(api.Contracts.Futures[code_list[i]][code_list[i] + '202310'].symbol)
            txt_name = str(api.Contracts.Futures[code_list[i]][code_list[i] + '202310'].name)
            print(txt_symbol)
            print(txt_name)
        
        file.write(str(code_list[i]) + " " +  txt_symbol + " " + txt_name + '\n')








