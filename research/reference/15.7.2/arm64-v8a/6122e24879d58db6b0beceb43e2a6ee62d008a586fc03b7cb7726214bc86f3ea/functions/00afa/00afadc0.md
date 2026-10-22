# 00afadc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00afadc0.md)

## 関数情報

~~~json
{
  "address": "00afadc0",
  "name": "std::__ndk1::__tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>>>::erase",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b3b2a44416db4aa321235c24e2feee11b642cf68f57084604e7cf08beac7249d",
  "source_text_sha256": "b3b2a44416db4aa321235c24e2feee11b642cf68f57084604e7cf08beac7249d"
}
~~~
## 呼び出し元

- [00bde8a0](../00bde/00bde8a0.md)

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bddcd0](../00bdd/00bddcd0.md)
- [00bde1e0](../00bde/00bde1e0.md)
- [00bde650](../00bde/00bde650.md)

## 疑似コード 1/1 / UTF-8 5412 bytes

~~~c

/* std::__ndk1::__tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,
   std::__ndk1::char_traits<char>, std::__ndk1::allocator<char> >,
   std::__ndk1::unique_ptr<firebase::app_common::AppData,
   std::__ndk1::default_delete<firebase::app_common::AppData> > >,
   std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>,
   std::__ndk1::allocator<char> >, std::__ndk1::__value_type<std::__ndk1::basic_string<char,
   std::__ndk1::char_traits<char>, std::__ndk1::allocator<char> >,
   std::__ndk1::unique_ptr<firebase::app_common::AppData,
   std::__ndk1::default_delete<firebase::app_common::AppData> > >,
   std::__ndk1::less<std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>,
   std::__ndk1::allocator<char> > >, true>,
   std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,
   std::__ndk1::char_traits<char>, std::__ndk1::allocator<char> >,
   std::__ndk1::unique_ptr<firebase::app_common::AppData,
   std::__ndk1::default_delete<firebase::app_common::AppData> > > >
   >::erase(std::__ndk1::__tree_const_iterator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,
   std::__ndk1::char_traits<char>, std::__ndk1::allocator<char> >,
   std::__ndk1::unique_ptr<firebase::app_common::AppData,
   std::__ndk1::default_delete<firebase::app_common::AppData> > >,
   std::__ndk1::__tree_node<std::__ndk1::__value_type<std::__ndk1::basic_string<char,
   std::__ndk1::char_traits<char>, std::__ndk1::allocator<char> >,
   std::__ndk1::unique_ptr<firebase::app_common::AppData,
   std::__ndk1::default_delete<firebase::app_common::AppData> > >, void*>*, long>) */

long * __thiscall
std::__ndk1::
__tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>>>
::erase(__tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>>>
        *this,__tree_node_base *param_2)

{
  long *plVar1;
  __tree_node_base *p_Var2;
  long lVar3;
  long *plVar4;
  void *pvVar5;
  
  plVar1 = *(long **)(param_2 + 8);
  if (*(long **)(param_2 + 8) == (long *)0x0) {
    p_Var2 = param_2 + 0x10;
    plVar4 = *(long **)p_Var2;
    if ((__tree_node_base *)*plVar4 != param_2) {
      do {
                    /* try { // try from 00afae00 to 00bfae07 has its CatchHandler @ 00aff4fc */
        lVar3 = *(long *)p_Var2;
        p_Var2 = (__tree_node_base *)(lVar3 + 0x10);
        plVar4 = *(long **)p_Var2;
      } while (*plVar4 != lVar3);
    }
  }
  else {
    do {
                    /* try { // try from 00afaddc to 00bfadef has its CatchHandler @ 00aff500 */
      plVar4 = plVar1;
      plVar1 = (long *)*plVar4;
    } while ((long *)*plVar4 != (long *)0x0);
  }
  if (*(__tree_node_base **)this == param_2) {
    *(long **)this = plVar4;
  }
                    /* try { // try from 00afae30 to 00bfae43 has its CatchHandler @ 00aff4f8 */
  *(long *)(this + 0x10) = *(long *)(this + 0x10) + -1;
  __tree_remove<std::__ndk1::__tree_node_base<void*>*>(*(__tree_node_base **)(this + 8),param_2);
  pvVar5 = *(void **)(param_2 + 0x38);
  *(undefined8 *)(param_2 + 0x38) = 0;
  if (pvVar5 != (void *)0x0) {
    firebase::Logger::~Logger((Logger *)((long)pvVar5 + 0x68));
    firebase::CleanupNotifier::~CleanupNotifier((CleanupNotifier *)((long)pvVar5 + 8));
    operator_delete(pvVar5);
  }
                    /* try { // try from 00afae64 to 00bfae6b has its CatchHandler @ 00aff4f4 */
  if (((byte)param_2[0x20] & 1) != 0) {
    operator_delete(*(void **)(param_2 + 0x30));
  }
  operator_delete(param_2);
  return plVar4;
}

~~~
