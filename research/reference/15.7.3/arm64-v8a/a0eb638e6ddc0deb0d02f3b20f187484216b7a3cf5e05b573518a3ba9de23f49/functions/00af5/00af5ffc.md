# 00af5ffc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00af5ffc",
  "name": "_ZN8firebase4util17JavaThreadContext6CancelEv",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ed28a2abb718edcf1ff404e8350c186595df512c80a1c87998c1aa8b90929e7f",
  "source_text_sha256": "ed28a2abb718edcf1ff404e8350c186595df512c80a1c87998c1aa8b90929e7f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00551e14](../00551/00551e14.md)
- [00bde310](../00bde/00bde310.md)

## 疑似コード / UTF-8 1224 bytes

~~~c

void _ZN8firebase4util17JavaThreadContext6CancelEv(long param_1)

{
  char cVar1;
  long *plVar2;
  
                    /* try { // try from 00af6000 to 00bf6007 has its CatchHandler @ 00affb00 */
  plVar2 = (long *)_ZNK8firebase8internal16JObjectReference9GetJNIEnvEv();
  if (*(long *)(param_1 + 8) != 0) {
    FUN_00551e14(plVar2,*(long *)(param_1 + 8),DAT_010a0390);
                    /* try { // try from 00af6028 to 00bf602f has its CatchHandler @ 00affaf8 */
    cVar1 = (**(code **)(*plVar2 + 0x720))(plVar2);
                    /* try { // try from 00af6038 to 00bf603f has its CatchHandler @ 00affaf0 */
    if (cVar1 != '\0') {
                    /* try { // try from 00af6048 to 00bf604f has its CatchHandler @ 00affae8 */
      (**(code **)(*plVar2 + 0x80))(plVar2);
                    /* try { // try from 00af6058 to 00bf605f has its CatchHandler @ 00affae0 */
                    /* WARNING: Could not recover jumptable at 0x00af6064. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      (**(code **)(*plVar2 + 0x88))(plVar2);
      return;
    }
  }
                    /* try { // try from 00af6068 to 00bf606f has its CatchHandler @ 00affad8 */
  return;
}

~~~
