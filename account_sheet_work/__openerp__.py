# -*- encoding: utf-8 -*-
{
	'name': 'Account Sheet Work IT',
	'category': 'account',
	'author': 'ITGRUPO-COMPATIBLE-BO',
	'depends': ['import_base_it','account_parametros_it'],
	'version': '1.0',
	'description':"""
	HOJA DE TRABAJO	
	
1.-  antes de crear la hoja de trabajo es necesario que se implemente un  campo en el formulario de  edición y creación de cuentas : 	
	
CLASIFICACIÓN HOJA DE TRABAJO: 	
	
	
	
	
	
	
	
2.- VISTAS QUE VAN A SACARSE : 	
	
A) BALANCE DE COMPROBACIÓN:   ES UN REPORTE QUE MOSTRARÁ  UN RESUMEN DE LOS MOVIMIENTOS DE UN DETERMINADO PERIODO O HASTA DETERMINADO PERIODO ESTO POR CUENTAS 	
EL WIZARD  PREVIO A ESTA VISTA ES LLAMDO POR EL MENÚ HOJA DE TRABAJO QUE SERÁ A SU VEZ UN SUBMENU DE ESTADOS FINANCIEROS SITUADO ENEL EMNU CONTABILIDAD INFORMES	
	
EL WIZARD TENDRA ESTOS CAMPOS : 	
	
PERIODO INCIAL 	
PERIODO FINAL 	
NIVEL A MOSTRAR : 	
	
MONEDA : 	
	
	
UNA VEZ SELECCIONADA LA OPCIÓN SE MOSTRARA UN RESUMEN  EN DONDE SE TOTALICE EL DEBE Y EL HABER DE CADA CUENTA Y LUEGO SE MUESTRE EL SALDO EN LAS COLUMNAS 	
SALDO DEUDOR O SALDO ACREEDOR SEGÚN LA SIGUIENTE FÓRMULA : 	
	
CUENTA	DESCRIPCIÓN
1011	caja mn
1012	caja me
1212	clientes
4212	proveedore
4511	deudas financieras
	
	
	TOTALES
	
ESTE REPORTE ESTARÁ EN EL MENU CONTABILIDAD/INFORMES/ESTADOS FIN/B. COMPROBACION	
B) HOJA DE TRABAJO : 	
	
LA HOJA DE TRABAJO ES TAMBIÉN UN RESUMEN DE LAS SUMAS DE LOS MOVIMIENTOS DE LAS CUENTAS CONTABLES Y TENDRA  EN SUS CUATRO COLUMNAS LA MISMA INFORMACIÓN DEL 	
BALANCE DE COMPROBACION ,  ADEMÁS TENDRA LS SIGUIENTES COLUMNAS 	
	
CUENTA	DESCRIPCIÓN
1011	caja mn
1012	caja me
1212	clientes
4212	proveedore
4511	deudas financieras
	
	
	TOTALES
	RESULTADO DEL PERIODO
	
LOS MONTOS ESTAN EN LAS COLUMNAS SALDO DEUDOR Y SALDO ACREEDOR SERAN DISTRIBUIDAS   UTILIZANDO LA CONFIGURACIÓN QUE TIENE CADA CUENTA :  	
	
SI ES DE TIPO  ESTADO DE SITUACIÓN : 	
SI ES DE TIPO RESULTADOS POR NATURALEZA : 	
SI ES DE TIPO RESULTADOS POR FUNCION : 	
SI ES CUENTA DE ORDEN SU SALDO NO SE DISTRIBUYE A NINGUNA COLUMNA 	
SI ES CUENTA DE MAYOR SU SALDO NO SE DISTRIBUYE A NINGUNA COLUMNA 	
	
AL FINAL AGREGAR UNA LÍNEA  CON LA SUMA TOTAL  DE CADA COLUMNA 	
LUEGO DE ESTA FILA AGREGAR OTRA EN DONDE SE PONDRÁ LO QUE SALGA DE LA RESTA DE ACTIVO - PASIVO ( SI ACTIVO ES MAYOR QUE PASIVO IRA DEBAJO DE PASIVO  DE LO CONTRARIO IRA DEBAJO DE ACTIVO) 	
EN LA MISMA FILA EXPLICADA ANTERIORMENTE AGREGAR LA DIFERENCIA DE GANANCIAS NAT - PERDIDAS NAT ( SI  GANANCIAS NAT ES MAYOR QUE PERDIDAS NAT LA CANTIAD IRA DEBAJO DE PERDIDAS NAT, CASO CONTRARIO EN GANANCIAS NAT) 	
EN LA MISMA FILA EXPLICADA ANTERIORMENTE AGREGAR LA DIFERENCIA DE GANANCIAS FUN - PERDIDAS FUN ( SI  GANANCIAS FUN ES MAYOR QUE PERDIDAS FUN  LA CANTIAD IRA DEBAJO DE PERDIDAS FUN. CASO CONTRARIO IRA EN GANANCIAS FUN	
	
ESTE REPORTE ESTARÁ EN EL MENU CONTABILIDAD/INFORMES/EE FF/HOJA DE TRABAJO	

	""",
	'auto_install': False,
	'demo': [],
	'data':	['account_sheet_work_view.xml','wizard/account_sheet_work_wizard_view.xml','wizard/account_sheet_work_detalle_wizard_view.xml'],
	'installable': True
}
