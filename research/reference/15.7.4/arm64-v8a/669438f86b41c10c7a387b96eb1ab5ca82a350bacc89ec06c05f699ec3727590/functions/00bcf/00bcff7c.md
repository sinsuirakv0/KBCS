# 00bcff7c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bcff7c",
  "name": "FUN_00bcff7c",
  "size": 280,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3fdf24343c0a0f0b0b608cf5b66fe640db640d3861eb4ca3ed9ee50cf6273e97",
  "source_text_sha256": "3fdf24343c0a0f0b0b608cf5b66fe640db640d3861eb4ca3ed9ee50cf6273e97"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

## 関連文字列（未確認候補）

~~~text
"::friend "
~~~

## 疑似コード / UTF-8 2397 bytes

~~~c

void FUN_00bcff7c(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  undefined8 uVar2;
  void *__ptr;
  long lVar3;
  size_t __size;
  long *plVar4;
  
  plVar4 = *(long **)(param_1 + 0x10);
                    /* try { // try from 00bcff98 to 00cd000f has its CatchHandler @ 00bcff98
                       catch() { ... } // from try @ 00bcff98 with catch @ 00bcff98
                       catch() { ... } // from try @ 00bd0070 with catch @ 00bcff98 */
  (**(code **)(*plVar4 + 0x20))(plVar4);
  if ((*(ushort *)((long)plVar4 + 9) & 0xc0) != 0x40) {
    (**(code **)(*plVar4 + 0x28))(plVar4,param_2);
  }
  lVar3 = param_2[1];
  __ptr = (void *)*param_2;
  if ((ulong)param_2[2] < lVar3 + 9U) {
    __size = param_2[2] * 2;
    uVar1 = lVar3 + 0x3e9;
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
  uVar2 = s___friend_0029577f._0_8_;
                    /* try { // try from 00bd0010 to 00cd0017 has its CatchHandler @ 00bd0250 */
                    /* try { // try from 00bd0018 to 00cd001f has its CatchHandler @ 00bd0230 */
                    /* try { // try from 00bd0020 to 00cd0027 has its CatchHandler @ 00bd0210 */
  ((char *)((long)__ptr + lVar3))[8] = ' ';
  *(undefined8 *)((long)__ptr + lVar3) = uVar2;
                    /* try { // try from 00bd0028 to 00cd002f has its CatchHandler @ 00bd01f0 */
  plVar4 = *(long **)(param_1 + 0x18);
                    /* try { // try from 00bd0030 to 00cd0053 has its CatchHandler @ 00bd01d0 */
  lVar3 = *plVar4;
  param_2[1] = param_2[1] + 9;
  (**(code **)(lVar3 + 0x20))(plVar4,param_2);
                    /* try { // try from 00bd0054 to 00cd005f has its CatchHandler @ 00bd0164 */
  if ((*(ushort *)((long)plVar4 + 9) & 0xc0) == 0x40) {
                    /* try { // try from 00bd0060 to 00cd006f has its CatchHandler @ 00bd0154 */
    return;
  }
                    /* try { // try from 00bd0070 to 00cd025f has its CatchHandler @ 00bcff98 */
                    /* WARNING: Could not recover jumptable at 0x00bd008c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar4 + 0x28))(plVar4,param_2);
  return;
}

~~~
