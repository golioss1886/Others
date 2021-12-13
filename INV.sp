.lib 'hspice.lib' tt
.PARAM
.option post

.GLOBAL gnd!
+		 vdd!


.SUBCKT INV input output
...
MM0 output input gnd! gnd! Nch W=220.00n L=180.00n
MM1 output input vdd! vdd! Pch W=420.00n L=180.00n
.ENDS

XINV input output INV
C0 output gnd! 2E-15F

Vvdd vdd! 0 1.0v
Vgnd gnd! 0 0v

V1 input 0 DC PWL 0, 1.0v, 950p, 1.8v, 1000p, 0v, 1950p, 0v, 2000p, 1.8v, 2950p, 1.8v, 3000p, 1.8v R 0

.tran 10p 10n
.END
