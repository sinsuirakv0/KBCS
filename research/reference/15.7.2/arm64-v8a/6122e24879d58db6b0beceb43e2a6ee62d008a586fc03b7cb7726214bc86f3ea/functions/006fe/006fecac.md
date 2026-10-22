# 006fecac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](006fecac.md)

## 関数情報

~~~json
{
  "address": "006fecac",
  "name": "FUN_006fecac",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "19a448a0de995e2672f1d23888f71c8aac32fae35b73841e5f00e2bbd27732cc",
  "source_text_sha256": "19a448a0de995e2672f1d23888f71c8aac32fae35b73841e5f00e2bbd27732cc"
}
~~~
## 呼び出し元

- [00734830](../00734/00734830.md)
- [0073496c](../00734/0073496c.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

## 疑似コード 1/1 / UTF-8 1140 bytes

~~~c

undefined4 FUN_006fecac(uint param_1)

{
  uint uVar1;
  long lVar2;
  long lVar3;
  
                    /* catch() { ... } // from try @ 006fe914 with catch @ 006fecac */
                    /* catch() { ... } // from try @ 006fe688 with catch @ 006fecb0 */
                    /* catch() { ... } // from try @ 006fea64 with catch @ 006fecb4
                       catch() { ... } // from try @ 006fec4c with catch @ 006fecb4 */
                    /* catch() { ... } // from try @ 006fea90 with catch @ 006fecbc */
  lVar2 = FUN_0081f580();
  lVar3 = FUN_0081f580();
                    /* catch() { ... } // from try @ 006fe9bc with catch @ 006feccc
                       catch() { ... } // from try @ 006fec34 with catch @ 006feccc */
                    /* catch() { ... } // from try @ 006fea04 with catch @ 006fecd4 */
  uVar1 = *(int *)(BYTE_ARRAY_00343241 + lVar3 + 0x23) + ~param_1 &
          ((int)(*(int *)(BYTE_ARRAY_00343241 + lVar3 + 0x23) + ~param_1) >> 0x1f ^ 0xffffffffU);
  if (0x1f2 < uVar1) {
    uVar1 = 499;
  }
  return *(undefined4 *)(&uleb128_00389fd0 + lVar2 + (ulong)uVar1 * 4);
}

~~~
