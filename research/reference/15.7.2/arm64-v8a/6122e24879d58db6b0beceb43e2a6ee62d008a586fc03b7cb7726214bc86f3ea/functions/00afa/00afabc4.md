# 00afabc4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00afabc4.md)

## 関数情報

~~~json
{
  "address": "00afabc4",
  "name": "std::__ndk1::__tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>>>::find<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d653f4f1538eb065bf7f5dc66cf8428e2d44506d205fc597608d64f94eae4ec2",
  "source_text_sha256": "d653f4f1538eb065bf7f5dc66cf8428e2d44506d205fc597608d64f94eae4ec2"
}
~~~
## 呼び出し元

- [00bde890](../00bde/00bde890.md)

## 呼び出し先

- [00bdb100](../00bdb/00bdb100.md)

## 疑似コード 1/1 / UTF-8 18389 bytes

~~~c

/* std::__ndk1::__tree_iterator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,
   std::__ndk1::char_traits<char>, std::__ndk1::allocator<char> >,
   std::__ndk1::unique_ptr<firebase::app_common::AppData,
   std::__ndk1::default_delete<firebase::app_common::AppData> > >,
   std::__ndk1::__tree_node<std::__ndk1::__value_type<std::__ndk1::basic_string<char,
   std::__ndk1::char_traits<char>, std::__ndk1::allocator<char> >,
   std::__ndk1::unique_ptr<firebase::app_common::AppData,
   std::__ndk1::default_delete<firebase::app_common::AppData> > >, void*>*, long>
   std::__ndk1::__tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,
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
   >::find<std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>,
   std::__ndk1::allocator<char> > >(std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>,
   std::__ndk1::allocator<char> > const&) */

__tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>>>
* __thiscall
std::__ndk1::
__tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>>>
::find<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>
          (__tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>>>
           *this,basic_string *param_1)

{
  ulong uVar1;
  size_t sVar2;
  ulong uVar3;
  basic_string *__s2;
  __tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>>>
  _Var4;
  uint uVar5;
  int iVar6;
  __tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>>>
  *__s1;
  __tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>>>
  *p_Var7;
  __tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>>>
  *p_Var8;
  __tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>>>
  *p_Var9;
  
                    /* try { // try from 00afabc4 to 00bfabcb has its CatchHandler @ 00b00238 */
  p_Var7 = this + 8;
  p_Var9 = *(__tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>>>
             **)p_Var7;
  if (p_Var9 != (__tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>>>
                 *)0x0) {
    uVar3 = *(ulong *)(param_1 + 8);
    __s2 = *(basic_string **)(param_1 + 0x10);
    p_Var8 = p_Var7;
    if (((byte)*param_1 & 1) == 0) {
      __s2 = param_1 + 1;
      uVar3 = (ulong)((byte)*param_1 >> 1);
    }
    do {
                    /* try { // try from 00afac28 to 00bfac33 has its CatchHandler @ 00b0023c */
      _Var4 = p_Var9[0x20];
      uVar1 = (ulong)((byte)_Var4 >> 1);
      if (((byte)_Var4 & 1) != 0) {
        uVar1 = *(ulong *)(p_Var9 + 0x28);
      }
      sVar2 = uVar3;
      if (uVar1 <= uVar3) {
        sVar2 = uVar1;
      }
      if (sVar2 == 0) {
LAB_00afac04:
        uVar5 = (uint)(uVar3 < uVar1);
                    /* try { // try from 00afac10 to 00bfac17 has its CatchHandler @ 00b001dc */
        if (uVar1 < uVar3) {
          uVar5 = 0xffffffff;
        }
      }
      else {
        __s1 = *(__tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>>>
                 **)(p_Var9 + 0x30);
        if (((byte)_Var4 & 1) == 0) {
          __s1 = p_Var9 + 0x21;
        }
        uVar5 = memcmp(__s1,__s2,sVar2);
        if (uVar5 == 0) goto LAB_00afac04;
      }
                    /* try { // try from 00afac18 to 00bfac27 has its CatchHandler @ 00b00254 */
      if ((int)uVar5 >= 0) {
        p_Var8 = p_Var9;
      }
      p_Var9 = *(__tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>>>
                 **)(p_Var9 + (ulong)((int)uVar5 < 0) * 8);
    } while (p_Var9 != (__tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>>>
                        *)0x0);
    if (p_Var8 != p_Var7) {
      _Var4 = p_Var8[0x20];
                    /* try { // try from 00afac7c to 00bfac9b has its CatchHandler @ 00afff3c */
      uVar1 = (ulong)((byte)_Var4 >> 1);
      if (((byte)_Var4 & 1) != 0) {
        uVar1 = *(ulong *)(p_Var8 + 0x28);
      }
      sVar2 = uVar1;
      if (uVar3 <= uVar1) {
        sVar2 = uVar3;
      }
      if (sVar2 != 0) {
        p_Var9 = *(__tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::unique_ptr<firebase::app_common::AppData,std::__ndk1::default_delete<firebase::app_common::AppData>>>>>
                   **)(p_Var8 + 0x30);
        if (((byte)_Var4 & 1) == 0) {
          p_Var9 = p_Var8 + 0x21;
        }
        iVar6 = memcmp(__s2,p_Var9,sVar2);
        if (iVar6 != 0) {
          if (iVar6 < 0) {
            return p_Var7;
          }
          return p_Var8;
        }
      }
      if (uVar1 <= uVar3) {
        return p_Var8;
      }
    }
  }
                    /* try { // try from 00afacc4 to 00bfacd3 has its CatchHandler @ 00aff514 */
  return p_Var7;
}

~~~
