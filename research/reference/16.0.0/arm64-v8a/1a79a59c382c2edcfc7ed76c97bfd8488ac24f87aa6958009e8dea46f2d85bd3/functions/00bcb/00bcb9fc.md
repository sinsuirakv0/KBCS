# 00bcb9fc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bcb9fc",
  "name": "_ZNSt6__ndk16vectorIPN8firebase4auth17AuthStateListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "06de6ac1902b25c066493372b9f37d084eb308a6c80f0323521ccb4d698ba5da",
  "source_text_sha256": "06de6ac1902b25c066493372b9f37d084eb308a6c80f0323521ccb4d698ba5da"
}
~~~

## 呼び出し元

- [00c5d6f0](../00c5d/00c5d6f0.md)

## 呼び出し先

- [00b3fe98](../00b3f/00b3fe98.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57c00](../00c57/00c57c00.md)
- [00c5a910](../00c5a/00c5a910.md)

## 関連文字列（未確認候補）

~~~text
"allocator<T>::allocate(size_t n) 'n' exceeds maximum supported size"
~~~

## 疑似コード / UTF-8 1949 bytes

~~~c

void _ZNSt6__ndk16vectorIPN8firebase4auth17AuthStateListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_
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
                    /* WARNING: Subroutine does not return */
    _ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv(param_1);
  }
                    /* catch() { ... } // from try @ 00bcb9cc with catch @ 00bcba30 */
  if ((ulong)(param_1[2] - (long)__src >> 3) < 0xfffffffffffffff) {
    uVar2 = param_1[2] - (long)__src >> 2;
    if (uVar3 <= uVar2) {
      uVar3 = uVar2;
    }
    if (uVar3 == 0) {
      __dest = (void *)0x0;
      goto LAB_00bcba7c;
    }
                    /* try { // try from 00bcba58 to 00ccbac3 has its CatchHandler @ 00bcba58
                       catch() { ... } // from try @ 00bcba58 with catch @ 00bcba58
                       catch() { ... } // from try @ 00bcbad0 with catch @ 00bcba58 */
    if (uVar3 >> 0x3d != 0) {
                    /* WARNING: Subroutine does not return */
      FUN_00b3fe98("allocator<T>::allocate(size_t n) \'n\' exceeds maximum supported size");
    }
  }
  else {
    uVar3 = 0x1fffffffffffffff;
  }
  __dest = (void *)_Znwm(uVar3 << 3);
LAB_00bcba7c:
  puVar1 = (undefined8 *)((long)__dest + ((long)__n >> 3) * 8);
  *puVar1 = *param_2;
  if (0 < (long)__n) {
    memcpy(__dest,__src,__n);
  }
  *param_1 = __dest;
  param_1[1] = puVar1 + 1;
  param_1[2] = (void *)((long)__dest + uVar3 * 8);
  if (__src != (void *)0x0) {
                    /* try { // try from 00bcbac4 to 00ccbacf has its CatchHandler @ 00bcbb28 */
    _ZdlPv(__src);
    return;
  }
                    /* try { // try from 00bcbad0 to 00ccbb4f has its CatchHandler @ 00bcba58 */
  return;
}

~~~
