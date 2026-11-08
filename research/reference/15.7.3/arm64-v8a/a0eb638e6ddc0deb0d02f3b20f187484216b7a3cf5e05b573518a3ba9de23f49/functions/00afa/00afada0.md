# 00afada0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00afada0",
  "name": "_ZNSt6__ndk16vectorIPN8firebase3AppENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "03b61cd3c8c0321e848bf6cf48449bce4150e5eb3a52ce31668952c2453e97fc",
  "source_text_sha256": "03b61cd3c8c0321e848bf6cf48449bce4150e5eb3a52ce31668952c2453e97fc"
}
~~~

## 呼び出し元

- [00bde970](../00bde/00bde970.md)

## 呼び出し先

- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bde270](../00bde/00bde270.md)

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
  
                    /* try { // try from 00afadac to 00bfadb3 has its CatchHandler @ 00aff504 */
  __src = (void *)*param_1;
  __n = param_1[1] - (long)__src;
  uVar3 = ((long)__n >> 3) + 1;
  if (uVar3 >> 0x3d != 0) {
LAB_00afae04:
                    /* WARNING: Subroutine does not return */
    abort();
  }
                    /* try { // try from 00afaddc to 00bfadef has its CatchHandler @ 00aff500 */
  if ((ulong)(param_1[2] - (long)__src >> 3) < 0xfffffffffffffff) {
    uVar2 = param_1[2] - (long)__src >> 2;
    if (uVar3 <= uVar2) {
      uVar3 = uVar2;
    }
    if (uVar3 == 0) {
      __dest = (void *)0x0;
      goto LAB_00afae18;
    }
                    /* try { // try from 00afae00 to 00bfae07 has its CatchHandler @ 00aff4fc */
    if (uVar3 >> 0x3d != 0) goto LAB_00afae04;
  }
  else {
    uVar3 = 0x1fffffffffffffff;
  }
  __dest = (void *)_Znwm(uVar3 << 3);
LAB_00afae18:
  puVar1 = (undefined8 *)((long)__dest + ((long)__n >> 3) * 8);
  *puVar1 = *param_2;
  if (0 < (long)__n) {
                    /* try { // try from 00afae30 to 00bfae43 has its CatchHandler @ 00aff4f8 */
    memcpy(__dest,__src,__n);
  }
  *param_1 = __dest;
  param_1[1] = puVar1 + 1;
  param_1[2] = (void *)((long)__dest + uVar3 * 8);
  if (__src != (void *)0x0) {
                    /* try { // try from 00afae64 to 00bfae6b has its CatchHandler @ 00aff4f4 */
    _ZdlPv(__src);
    return;
  }
  return;
}

~~~
