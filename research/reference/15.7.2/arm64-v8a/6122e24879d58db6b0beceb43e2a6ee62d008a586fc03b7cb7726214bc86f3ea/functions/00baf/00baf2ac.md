# 00baf2ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baf2ac.md)

## 関数情報

~~~json
{
  "address": "00baf2ac",
  "name": "std::__ndk1::numpunct_byname<char>::__init",
  "size": 600,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "93398b1405aec22db6b0da85971f8755339af00137a5ec04982381b975b8fac5",
  "source_text_sha256": "93398b1405aec22db6b0da85971f8755339af00137a5ec04982381b975b8fac5"
}
~~~
## 呼び出し元

- [00be1b70](../00be1/00be1b70.md)

## 呼び出し先

- [0041b298](../0041b/0041b298.md)
- [0041e0fc](../0041e/0041e0fc.md)
- [00b7501c](../00b75/00b7501c.md)
- [00ba89b8](../00ba8/00ba89b8.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bde8d0](../00bde/00bde8d0.md)
- [00be0eb0](../00be0/00be0eb0.md)
- [00be1470](../00be1/00be1470.md)
- [00be1480](../00be1/00be1480.md)
- [00be1830](../00be1/00be1830.md)
- [00be1a10](../00be1/00be1a10.md)
- [00be1a70](../00be1/00be1a70.md)
- [00be1b80](../00be1/00be1b80.md)

## 関連文字列（未確認候補）

~~~text
"numpunct_byname<char>::numpunct_byname failed to construct for "
~~~
## 疑似コード 1/1 / UTF-8 3808 bytes

~~~c

/* std::__ndk1::numpunct_byname<char>::__init(char const*) */

void __thiscall
std::__ndk1::numpunct_byname<char>::__init(numpunct_byname<char> *this,char *param_1)

{
  wchar_t __c;
  int iVar1;
  __locale_t __dataset;
  __locale_t p_Var2;
  lconv *plVar3;
  size_t sVar4;
  numpunct_byname<char> *pnVar5;
  mbstate_t local_80 [3];
  undefined8 local_68;
  char *local_58;
  __locale_t local_50;
  wchar_t local_44;
  
  iVar1 = strcmp(param_1,"C");
  if (iVar1 != 0) {
    __dataset = newlocale(0x1fbf,param_1,(__locale_t)0x0);
    local_50 = __dataset;
    if (__dataset == (__locale_t)0x0) {
      FUN_0041b298(local_80,param_1);
                    /* try { // try from 00baf4e0 to 00caf583 has its CatchHandler @ 00baf60c */
      FUN_00ba89b8(&local_68,"numpunct_byname<char>::numpunct_byname failed to construct for ",
                   local_80);
      if (((byte)local_68 & 1) == 0) {
        local_58 = (char *)((long)&local_68 + 1);
      }
      __throw_runtime_error(local_58);
                    /* WARNING: Subroutine does not return */
      FUN_0041e0fc();
    }
    p_Var2 = uselocale(__dataset);
    local_68 = p_Var2;
    plVar3 = localeconv();
    if (p_Var2 != (__locale_t)0x0) {
      uselocale(p_Var2);
    }
    pnVar5 = (numpunct_byname<char> *)plVar3->decimal_point;
    if (*pnVar5 != (numpunct_byname<char>)0x0) {
      if (pnVar5[1] == (numpunct_byname<char>)0x0) {
        this[0x10] = *pnVar5;
      }
      else {
        local_80[0].__count = 0;
        local_80[0].__value = (_union_27)0x0;
        sVar4 = strlen((char *)pnVar5);
        p_Var2 = uselocale(__dataset);
        local_68 = p_Var2;
        sVar4 = mbrtowc(&local_44,(char *)pnVar5,sVar4,local_80);
        if (p_Var2 != (__locale_t)0x0) {
          uselocale(p_Var2);
        }
        __c = local_44;
                    /* catch() { ... } // from try @ 00baf20c with catch @ 00baf378 */
        if (sVar4 < 0xfffffffffffffffe) {
          p_Var2 = uselocale(__dataset);
          local_68 = p_Var2;
          iVar1 = wctob(__c);
          if (p_Var2 != (__locale_t)0x0) {
            uselocale(p_Var2);
          }
          if (((iVar1 != -1) || (iVar1 = 0x20, __c == L'\x202f')) || (__c == L'\xa0')) {
            this[0x10] = SUB41(iVar1,0);
          }
        }
      }
    }
    pnVar5 = (numpunct_byname<char> *)plVar3->thousands_sep;
    if (*pnVar5 != (numpunct_byname<char>)0x0) {
      if (pnVar5[1] == (numpunct_byname<char>)0x0) {
        this[0x11] = *pnVar5;
      }
      else {
        local_80[0].__count = 0;
        local_80[0].__value = (_union_27)0x0;
        sVar4 = strlen((char *)pnVar5);
        p_Var2 = uselocale(__dataset);
        local_68 = p_Var2;
        sVar4 = mbrtowc(&local_44,(char *)pnVar5,sVar4,local_80);
        if (p_Var2 != (__locale_t)0x0) {
          uselocale(p_Var2);
        }
        if (sVar4 < 0xfffffffffffffffe) {
          p_Var2 = uselocale(__dataset);
          local_68 = p_Var2;
          iVar1 = wctob(local_44);
          if (p_Var2 != (__locale_t)0x0) {
                    /* catch() { ... } // from try @ 00baf584 with catch @ 00baf448
                       catch() { ... } // from try @ 00baf600 with catch @ 00baf448 */
            uselocale(p_Var2);
          }
                    /* try { // try from 00baf4bc to 00caf4d7 has its CatchHandler @ 00baf608 */
          if (((iVar1 != -1) || (iVar1 = 0x20, local_44 == L'\x202f')) || (local_44 == L'\xa0')) {
            this[0x11] = SUB41(iVar1,0);
          }
        }
      }
    }
    FUN_00b7501c(this + 0x18,plVar3->grouping);
    freelocale(__dataset);
  }
                    /* try { // try from 00baf480 to 00caf49b has its CatchHandler @ 00baf600 */
  return;
}

~~~
