# 00bcb4bc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bcb4bc",
  "name": "_ZNSt6__ndk16vectorIPN8firebase4auth15IdTokenListenerENS_9allocatorIS4_EEEC2ERKS7_",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7c03bd111398704ff81fd2bfd2c41600877c102be28b57c67687f464d43c3bb9",
  "source_text_sha256": "7c03bd111398704ff81fd2bfd2c41600877c102be28b57c67687f464d43c3bb9"
}
~~~

## 呼び出し元

- [00c5d6e0](../00c5d/00c5d6e0.md)

## 呼び出し先

- [00c57a90](../00c57/00c57a90.md)
- [00c57c00](../00c57/00c57c00.md)
- [00c5a910](../00c5a/00c5a910.md)

## 疑似コード / UTF-8 911 bytes

~~~c

void _ZNSt6__ndk16vectorIPN8firebase4auth15IdTokenListenerENS_9allocatorIS4_EEEC2ERKS7_
               (undefined8 *param_1,long *param_2)

{
  void *__dest;
  size_t __n;
  ulong uVar1;
  
                    /* catch() { ... } // from try @ 00bcb6a8 with catch @ 00bcb4cc */
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  if (param_2[1] - *param_2 != 0) {
    uVar1 = param_2[1] - *param_2 >> 3;
    if (uVar1 >> 0x3d != 0) {
                    /* WARNING: Subroutine does not return */
      _ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv(param_1);
    }
    __dest = (void *)_Znwm();
    *param_1 = __dest;
    param_1[1] = __dest;
    param_1[2] = (void *)((long)__dest + uVar1 * 8);
    __n = param_2[1] - *param_2;
    if (0 < (long)__n) {
      memcpy(__dest,(void *)*param_2,__n);
      __dest = (void *)((long)__dest + __n);
    }
    param_1[1] = __dest;
  }
  return;
}

~~~
