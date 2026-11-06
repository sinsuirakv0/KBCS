# 00bcf1ec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00bcf1ec.md)

## 関数情報

~~~json
{
  "address": "00bcf1ec",
  "name": "FUN_00bcf1ec",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "17b59d3062aff8f6cf15e132823076dbc82d962ff73f13d0288683c51c407e24",
  "source_text_sha256": "17b59d3062aff8f6cf15e132823076dbc82d962ff73f13d0288683c51c407e24"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

## 関連文字列（未確認候補）

~~~text
"operator\"\" "
~~~
## 疑似コード 1/1 / UTF-8 1908 bytes

~~~c

void FUN_00bcf1ec(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  char *pcVar2;
  void *__ptr;
  long lVar3;
  size_t __size;
  long *plVar4;
  
  lVar3 = param_2[1];
  __ptr = (void *)*param_2;
  if ((ulong)param_2[2] < lVar3 + 0xbU) {
    __size = param_2[2] * 2;
    uVar1 = lVar3 + 0x3eb;
    if (__size < uVar1 || __size - uVar1 == 0) {
      __size = uVar1;
    }
    param_2[2] = __size;
    __ptr = realloc(__ptr,__size);
    *param_2 = __ptr;
    if (__ptr == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar3 = param_2[1];
  }
                    /* catch() { ... } // from try @ 00bcf01c with catch @ 00bcf248 */
                    /* catch() { ... } // from try @ 00bcf00c with catch @ 00bcf24c */
  pcVar2 = (char *)((long)__ptr + lVar3);
                    /* catch() { ... } // from try @ 00bcf000 with catch @ 00bcf250 */
                    /* catch() { ... } // from try @ 00bcefc8 with catch @ 00bcf254 */
                    /* catch() { ... } // from try @ 00bceeb0 with catch @ 00bcf258 */
  *(undefined8 *)pcVar2 = s_operator___002ab3aa._0_8_;
  pcVar2[7] = 'r';
  pcVar2[8] = '\"';
  pcVar2[9] = '\"';
  pcVar2[10] = ' ';
  plVar4 = *(long **)(param_1 + 0x10);
  lVar3 = *plVar4;
  param_2[1] = param_2[1] + 0xb;
  (**(code **)(lVar3 + 0x20))(plVar4,param_2);
                    /* catch() { ... } // from try @ 00bceea0 with catch @ 00bcf28c */
  if ((*(ushort *)((long)plVar4 + 9) & 0xc0) == 0x40) {
    return;
  }
                    /* catch() { ... } // from try @ 00bcee94 with catch @ 00bcf2ac */
                    /* catch() { ... } // from try @ 00bcedd4 with catch @ 00bcf2c0 */
                    /* WARNING: Could not recover jumptable at 0x00bcf2c4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar4 + 0x28))(plVar4,param_2);
  return;
}

~~~
