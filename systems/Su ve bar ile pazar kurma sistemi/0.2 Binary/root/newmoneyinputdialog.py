import uiScriptLocale

window = {
	"name" : "InputDialog",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : 200 + 30 + 10,
	"height" : 200 + 35,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : 200 + 30 + 10,
			"height" : 200 + 50,

			"title" : "",

			"children" :
			(

				## Input Slot
				{
					"name" : "InputSlot",
					"type" : "slotbar",

					"x" : 0,
					"y" : 34,
					"width" : 90,
					"height" : 18,
					"horizontal_align" : "center",
					
					"text" : "0",
					
					"children" :
					(
						{
							"name" : "InputValue",
							"type" : "editline",

							"x" : 3,
							"y" : 3,

							"width" : 90,
							"height" : 18,

							"input_limit" : 12,
						},
					),
				},

				## Input Slot
				
				## Input Slot2
				{
					"name" : "InputSlot1",
					"type" : "slotbar",

					"x" : 0,
					"y" : 34+25,
					"width" : 90,
					"height" : 18,
					"horizontal_align" : "center",
					
					"text" : "0",
					
					"children" :
					(
						{
							"name" : "InputValue1",
							"type" : "editline",

							"x" : 3,
							"y" : 3,

							"width" : 90,
							"height" : 18,

							"input_limit" : 12,
						},
					),
				},

				## Input Slot2
				
				## Input Slot3
				{
					"name" : "InputSlot2",
					"type" : "slotbar",

					"x" : 0,
					"y" : 34+15+35,
					"width" : 90,
					"height" : 18,
					"horizontal_align" : "center",

					"text" : "0",
					
					"children" :
					(
						{
							"name" : "InputValue2",
							"type" : "editline",

							"x" : 3,
							"y" : 3,

							"width" : 90,
							"height" : 18,

							"input_limit" : 12,
						},
					),
				},

				## Input Slot3
				{
					"name":"Dikkat",
					"type":"text",
					
					"text":"|cffffcc00ÖNEMLÝ;",
					
					"x":0,
					"y":59+15+15+10+10,
					
					"fontsize":"LARGE",

					"text_horizontal_align":"center",
					"horizontal_align":"center"
				},
				{
					"name" : "Dikkat2",
					"type" : "text",

					"x" : 0,
					"y" : 59+15+15+20+15,

					"fontsize":"LARGE",

					"text" : "|cFF90EE90Envanterin Tamamen Doluysa",

					"text_horizontal_align" : "center",
					"horizontal_align" : "center",
				},
				{
					"name" : "Dikkat3",
					"type" : "text",

					"x" : 0,
					"y" : 59+15+15+28+20,

					"fontsize":"LARGE",

					"text" : "|cFF90EE90Satýlýp Gelen Eþyalar Yere Düþer.",

					"text_horizontal_align" : "center",
					"horizontal_align" : "center",
				},

				{
					"name" : "MoneyValue",
					"type" : "text",

					"x" : 0,
					"y" : 59+15+15+38+35,
					"text" : "999999999",
					"text_horizontal_align" : "center",
					"horizontal_align" : "center",
				},
				
				{
					"name" : "MoneyValue1",
					"type" : "text",

					"x" : 0,
					"y" : 59+15+15+48+40,
					"text" : "199",
					"text_horizontal_align" : "center",
					"horizontal_align" : "center",
				},
		
				{
					"name" : "MoneyValue2",
					"type" : "text",

					"x" : 0,
					"y" : 59+15+15+58+45,
					"text" : "199",
					"text_horizontal_align" : "center",
					"horizontal_align" : "center",
				},

				## Button
				{
					"name" : "AcceptButton",
					"type" : "button",

					"x" : - 61 - 5 + 30,
					"y" : 78+30+55+15+40,
					"horizontal_align" : "center",

					"text" : uiScriptLocale.OK,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "CancelButton",
					"type" : "button",

					"x" : 5 + 30,
					"y" : 78+30+55+15+40,
					"horizontal_align" : "center",

					"text" : uiScriptLocale.CANCEL,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
			),
		},
	),
}