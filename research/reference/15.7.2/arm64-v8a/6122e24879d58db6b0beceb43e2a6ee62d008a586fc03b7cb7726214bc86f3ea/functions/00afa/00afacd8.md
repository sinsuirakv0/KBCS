# 00afacd8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00afacd8",
  "name": "_ZNSt6__ndk16vectorIPN8firebase3AppENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e12a6bcddbcd7407504aadc17f491c3437d566b904cc37e9cf974260c6b311c0",
  "source_text_sha256": "e12a6bcddbcd7407504aadc17f491c3437d566b904cc37e9cf974260c6b311c0"
}
~~~

## 呼び出し元

- [00bde8c0](../00bde/00bde8c0.md)

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)
- [00bde1c0](../00bde/00bde1c0.md)

## 疑似コード / UTF-8 1671 bytes

~~~c

void _ZNSt6__ndk16vectorIPN8firebase3AppENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_
               (undefined8 *param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  void *__src;
  void *__dest;
  ulong uVar2;
  size_t __n;
  ulong uVar3;
  
  __src = (void *)*param_1;
  __n = param_1[1] - (long)__src;
  uVar3 = ((long)__n >> 3) + 1;
  if (uVar3 >> 0x3d != 0) {
LAB_00afad3c:
                    /* WARNING: Subroutine does not return */
    abort();
  }
                    /* try { // try from 00afad10 to 00bfad23 has its CatchHandler @ 00aff510 */
  if ((ulong)(param_1[2] - (long)__src >> 3) < 0xfffffffffffffff) {
    uVar2 = param_1[2] - (long)__src >> 2;
    if (uVar3 <= uVar2) {
      uVar3 = uVar2;
    }
    if (uVar3 == 0) {
      __dest = (void *)0x0;
      goto LAB_00afad50;
    }
                    /* try { // try from 00afad34 to 00bfad3b has its CatchHandler @ 00aff50c */
    if (uVar3 >> 0x3d != 0) goto LAB_00afad3c;
  }
  else {
    uVar3 = 0x1fffffffffffffff;
  }
  __dest = (void *)_Znwm(uVar3 << 3);
LAB_00afad50:
  puVar1 = (undefined8 *)((long)__dest + ((long)__n >> 3) * 8);
  *puVar1 = *param_2;
                    /* try { // try from 00afad64 to 00bfad77 has its CatchHandler @ 00aff508 */
  if (0 < (long)__n) {
    memcpy(__dest,__src,__n);
  }
  *param_1 = __dest;
  param_1[1] = puVar1 + 1;
  param_1[2] = (void *)((long)__dest + uVar3 * 8);
  if (__src != (void *)0x0) {
                    /* try { // try from 00afad88 to 00bfadab has its CatchHandler @ 00b0037c */
    _ZdlPv(__src);
    return;
  }
                    /* try { // try from 00afadac to 00bfadb3 has its CatchHandler @ 00aff504 */
  return;
}

~~~
