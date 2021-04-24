# def add(vout):
#     if (vout > 0):
#         sign = 8;
#     elif (vout < 0):
#         sign = 9;
#     if (vout == 5):
#         v_rpp=23
#         RR=42
#         f=42
#         v_in=42
#         Tj_max=62
#         Ta=52
#         Pd=43
#         v_in_min = (int(vout) + dp + 1)
#         v_rpp_in_max = (v_rpp * ((10 ** RR) ** 1 / 20))
#         v_in_max = (v_in_min + (v_rpp_in_max / 2) + 2 + 1)
#         c = 1 /(2 * f * v_rpp_in_max)
#         v_rpp_in_max = 1 /( 2 * f * c)
#         i_d_avg = (1 * (1 + (2 * float(3.14)(v_in_max)) / (2 * v_rpp_in_max)) ** 0.5)
#         i_d_peak = (1 + (2 * float(3.14)(v_in_max / 2 * v_rpp_in_max)))
#         v_rms = (((v_in_max + 2 + v_rpp) * (v_in + 10)) / (1.414 * 0.95 * (v_in - 10)))
#         va =( v_rms * i_d_avg)
#         n = (v_in / v_rms)
#         Pd = (v_in_min - int(vout)
#         T_ja_cal = ((Tj_max - Ta) / (Pd))
#         if T_ja_cal < T_ja_device:
#             T_hsa = (T_ja_cal - T_jc - T_chs)
#         '''print(7, sign, 0, 5)'''
        
    


# def major():
#     v_in_min = (v4 + dp + 1);
#     v_rpp_in_max = (v_rpp * ((10 ^ RR) ^ 1 / 20));
#     v_in_max = (v_in_min + (v_rpp_in_max / 2) + 2 + 1);
#     c = 1 /(2 * f * v_rpp_in_max);
#     v_rpp_in_max = 1 /( 2 * f * c);
#     i_d_avg = (1 * (1 + (2 * float(3.14)(v_in_max)) / (2 * v_rpp_in_max)) ^ 0.5);
#     i_d_peak = (1 + (2 * float(3.14)(v_in_max / 2 * v_rpp_in_max)));
#     v_rms = (((v_in_max + 2 + v_rpp) * (v_in + 10)) / (1.414 * 0.95 * (v_in - 10)));
#     va =( v_rms * i_d_avg);
#     n = (v_in / v_rms);
#     Pd = (v_in_min - v4);
#     T_ja_cal = ((Tj_max - Ta) / (Pd));
#     if T_ja_cal < T_ja_device:
#         T_hsa = (T_ja_cal - T_jc - T_chs);

#     #  print("select heat-sink of T_HSA less than equal to" )
  


# def constant():
#     if (v4 > 0):
#         sign = 8;
#     elif (v4 < 0):
#         sign = 9;
    

#     if (v4 == 5):
#         '''print(7, sign, 0, 5)'''
#         major()
#     else:
#         if (v4 == 12):
#             '''print(7, sign, 1, 2)'''

#             major()
#         elif (v4 == 15):
#             '''print(7, sign, 1, 5)'''
#             major()

#         else:
#             if (sign == 8):
#                ''' print("LM317")'''
#                major()
#                R= ((v4/1.25) - 1);
#             else:
#                ''' print("LM337")'''
#                major()
#                R = (-1 - (v4 / 1.25));




# def variable(**var):
#     vout = ()
#     sign = ()
#     if (vout > 0):
#         sign = 8;
#     elif (vout < 0):
#         sign = 9;
#     else:
#         '''''print("lm317 and lm337")'''''
#         major()
#         r_317=((vout / 1.25) - 1);
#         r_337 = (-1 - (vout / 1.25));
#         '''''print(r)'''''
#     if (vout == 5):
#         '''''print(7, sign, 0, 5)'''''
#         major()
#     else:
#         if (vout == 12):
#             '''''print(7, sign, 1, 2)'''''
#             major()
#         elif (vout == 15):
#             '''''print(7, sign, 1, 5)'''''
#             major()

#         else:
#             if (sign == 8):
#                 '''''print("LM317")'''''
#                 major()
#                 r_317 = ((vout / 1.25) - 1);

#             else:
#                 '''''print("LM337")'''''
#                 major()
#                 r_337 = (-1 - (vout / 1.25));

    

#     
vout=5.0    
dp=20.0
v_rpp=23.0
RR=42.0
f=42.0
v_in=42.0
Tj_max=62.0
Ta=52.0
Pd=43.0
v_in_min = (float(vout) + dp + 1.0)
v_rpp_in_max = float(v_rpp * ((10.0 ** RR) ** 1.0 / 20.0))
v_in_max = float(v_in_min + (v_rpp_in_max / 2.0) + 2.0 + 1.0)
c = float(1.0 /(2.0 * f * v_rpp_in_max))
v_rpp_in_max = float(1.0 /( 2.0 * f * c))
i_d_avg = float(1.0 * (1.0 + (2.0 * 3.14 * float(v_in_max)) / (2.0 * v_rpp_in_max)) ** 0.5)
i_d_peak = float(1.0 + (2.0 * float(3.14)*(v_in_max / 2.0 * v_rpp_in_max)))
v_rms = (((v_in_max + 2.0 + v_rpp) * (v_in + 10.0)) / (1.414 * 0.95 * (v_in - 10.0)))
va =( v_rms * i_d_avg)
print(va)