import uiScriptLocale

window = {
	"name" : "InputDialog",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : 250,
	"height" : 380,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : 250,
			"height" : 380,

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
						{
							"name":"Money_Icon",
							"type":"image",

							"x" : -20,
							"y" : 3,

							"width" : 90,
							"height" : 18,

							"input_limit" : 12,

							"image":"d:/ymir work/ui/game/windows/money_icon.sub",
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
						{
							"name":"Money_Icon",
							"type":"image",

							"x" : -25,
							"y" : -3,

							"width" : 90,
							"height" : 18,

							"input_limit" : 12,

							"image":"d:/ymir work/ui/umut_baba/27991.tga",
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
						{
							"name":"Money_Icon",
							"type":"image",

							"x" : -20,
							"y" : 0,

							"width" : 90,
							"height" : 18,

							"input_limit" : 12,

							"image":"d:/ymir work/ui/umut_baba/80007.tga",
						},
					),
				},
				## Input Slot3
				{
					"name" : "InputSlot3",
					"type" : "slotbar",

					"x" : 0,
					"y" : 34+15+35+25,
					"width" : 90,
					"height" : 18,
					"horizontal_align" : "center",

					"children" :
					(
						{
							"name" : "InputValue3",
							"type" : "editline",

							"x" : 3,
							"y" : 3,

							"width" : 90,
							"height" : 18,

							"input_limit" : 12,
						},
						{
							"name":"Money_Icon",
							"type":"image",

							"x" : -20,
							"y" : 0,

							"width" : 90,
							"height" : 18,

							"input_limit" : 12,

							"image":"d:/ymir work/ui/umut_baba/70253.tga",
						},
					),
				},
				## Input Slot3
				{
					"name" : "InputSlot4",
					"type" : "slotbar",

					"x" : 0,
					"y" : 34+15+35+50,
					"width" : 90,
					"height" : 18,
					"horizontal_align" : "center",

					"children" :
					(
						{
							"name" : "InputValue4",
							"type" : "editline",

							"x" : 3,
							"y" : 3,

							"width" : 90,
							"height" : 18,

							"input_limit" : 12,
						},
						{
							"name":"Money_Icon",
							"type":"image",

							"x" : -20,
							"y" : 0,

							"width" : 90,
							"height" : 18,

							"input_limit" : 12,

							"image":"d:/ymir work/ui/umut_baba/70251.tga",
						},
					),
				},
				## Input Slot3
				{
					"name" : "InputSlot5",
					"type" : "slotbar",

					"x" : 0,
					"y" : 34+15+35+75,
					"width" : 90,
					"height" : 18,
					"horizontal_align" : "center",

					"children" :
					(
						{
							"name" : "InputValue5",
							"type" : "editline",

							"x" : 3,
							"y" : 3,

							"width" : 90,
							"height" : 18,

							"input_limit" : 12,
						},
						{
							"name":"Money_Icon",
							"type":"image",

							"x" : -20,
							"y" : 0,

							"width" : 90,
							"height" : 18,

							"input_limit" : 12,

							"image":"d:/ymir work/ui/umut_baba/70252.tga",
						},
					),
				},
				## Input Slot3
				{
					"name" : "InputSlot6",
					"type" : "slotbar",

					"x" : 0,
					"y" : 34+15+35+100,
					"width" : 90,
					"height" : 18,
					"horizontal_align" : "center",

					"children" :
					(
						{
							"name" : "InputValue6",
							"type" : "editline",

							"x" : 3,
							"y" : 3,

							"width" : 90,
							"height" : 18,

							"input_limit" : 12,
						},
						{
							"name":"Money_Icon",
							"type":"image",

							"x" : -20,
							"y" : 0,

							"width" : 90,
							"height" : 18,

							"input_limit" : 12,

							"image":"d:/ymir work/ui/umut_baba/70254.tga",
						},
					),
				},
				## Input Slot3
				{
					"name" : "InputSlot7",
					"type" : "slotbar",

					"x" : 0,
					"y" : 34+15+35+125,
					"width" : 90,
					"height" : 18,
					"horizontal_align" : "center",

					"children" :
					(
						{
							"name" : "InputValue7",
							"type" : "editline",

							"x" : 3,
							"y" : 3,

							"width" : 90,
							"height" : 18,

							"input_limit" : 12,
						},
						{
							"name":"Money_Icon",
							"type":"image",

							"x" : -20,
							"y" : 0,

							"width" : 90,
							"height" : 18,

							"input_limit" : 12,

							"image":"d:/ymir work/ui/umut_baba/50513.tga",
						},
					),
				},

				## Input Slot3
				
				{
					"name" : "MoneyValue",
					"type" : "text",

					"x" : 0,
					"y" : 59+15+15+140,
					"text" : "999999999",
					"text_horizontal_align" : "center",
					"horizontal_align" : "center",
				},
				
				{
					"name" : "MoneyValue1",
					"type" : "text",

					"x" : 0,
					"y" : 59+15+15+155,
					"text" : "999999999",
					"text_horizontal_align" : "center",
					"horizontal_align" : "center",
				},
		
				{
					"name" : "MoneyValue2",
					"type" : "text",

					"x" : 0,
					"y" : 59+15+15+170,
					"text" : "999999999",
					"text_horizontal_align" : "center",
					"horizontal_align" : "center",
				},
				{
					"name" : "MoneyValue3",
					"type" : "text",

					"x" : 0,
					"y" : 59+15+15+185,
					"text" : "999999999",
					"text_horizontal_align" : "center",
					"horizontal_align" : "center",
				},
				{
					"name" : "MoneyValue4",
					"type" : "text",

					"x" : 0,
					"y" : 59+15+15+200,
					"text" : "999999999",
					"text_horizontal_align" : "center",
					"horizontal_align" : "center",
				},
				{
					"name" : "MoneyValue5",
					"type" : "text",

					"x" : 0,
					"y" : 59+15+15+215,
					"text" : "999999999",
					"text_horizontal_align" : "center",
					"horizontal_align" : "center",
				},
				{
					"name" : "MoneyValue6",
					"type" : "text",

					"x" : 0,
					"y" : 59+15+15+230,
					"text" : "999999999",
					"text_horizontal_align" : "center",
					"horizontal_align" : "center",
				},
				{
					"name" : "MoneyValue7",
					"type" : "text",

					"x" : 0,
					"y" : 59+15+15+245,
					"text" : "999999999",
					"text_horizontal_align" : "center",
					"horizontal_align" : "center",
				},
				## Button
				{
					"name" : "AcceptButton",
					"type" : "button",

					"x" : - 61 - 5 + 30,
					"y" : 78+30+240,
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
					"y" : 78+30+240,
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