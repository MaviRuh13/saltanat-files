// Arat :
// PyObject * playerGetElk(PyObject* poSelf, PyObject* poArgs)
// Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
PyObject * playerGetDragonCoin(PyObject* poSelf, PyObject* poArgs)
{
	return Py_BuildValue("i", CPythonPlayer::Instance().GetDragonCoin());
}

PyObject * playerGetDragonMark(PyObject* poSelf, PyObject* poArgs)
{
	return Py_BuildValue("i", CPythonPlayer::Instance().GetDragonMark());
}
#endif

// Arat :
// { "GetMoney",					playerGetElk,						METH_VARARGS },
// Altýna Ekle :

#ifdef ENABLE_2TH_SHOPEX_SYSTEM
		{ "GetDragonCoin",				playerGetDragonCoin,				METH_VARARGS },
		{ "GetDragonMark",				playerGetDragonMark,				METH_VARARGS },
#endif