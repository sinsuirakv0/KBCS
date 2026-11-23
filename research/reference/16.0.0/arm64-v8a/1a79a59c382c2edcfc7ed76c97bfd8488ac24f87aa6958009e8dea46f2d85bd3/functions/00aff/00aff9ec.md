# 00aff9ec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/review-0170.md#review-d19eea21fdd9fd5b1705a53195a83aa3)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aff9ec",
  "name": "FUN_00aff9ec",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e99e491ae8a8c1d1b931a9889376936d86cb948746340a3d5c9f7ebbb69586f3",
  "source_text_sha256": "e99e491ae8a8c1d1b931a9889376936d86cb948746340a3d5c9f7ebbb69586f3"
}
~~~

## 呼び出し元

- [00a4f1bc](../00a4f/00a4f1bc.md)

## 呼び出し先

- [005e73e0](../005e7/005e73e0.md)
- [008514b8](../00851/008514b8.md)
- [00afe6c0](../00afe/00afe6c0.md)

## 疑似コード / UTF-8 1446 bytes

~~~c

int FUN_00aff9ec(int param_1,int param_2,int param_3)

{
  int iVar1;
  int iVar2;
  long lVar3;
  ulong uVar4;
  
                    /* catch() { ... } // from try @ 00aff874 with catch @ 00affa04 */
                    /* catch() { ... } // from try @ 00aff7ec with catch @ 00affa08 */
  lVar3 = FUN_008514b8();
                    /* catch() { ... } // from try @ 00aff820 with catch @ 00affa10 */
                    /* catch() { ... } // from try @ 00aff62c with catch @ 00affa18 */
                    /* catch() { ... } // from try @ 00aff5d8 with catch @ 00affa1c */
  uVar4 = FUN_005e73e0(lVar3 + (long)param_1 * 0x1f0 + 0x2768);
  lVar3 = FUN_008514b8();
  if ((uVar4 & 1) == 0) {
                    /* catch() { ... } // from try @ 00aff5cc with catch @ 00affa34 */
    iVar1 = *(int *)((long)__DT_JMPREL + lVar3 + ((long)param_2 + 2) * 0x1c4 + 0x1808);
                    /* catch() { ... } // from try @ 00aff594 with catch @ 00affa48 */
  }
  else {
                    /* catch() { ... } // from try @ 00aff4e4 with catch @ 00affa4c */
                    /* catch() { ... } // from try @ 00aff4d0 with catch @ 00affa60 */
    iVar1 = *(int *)(lVar3 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f6e0);
    iVar2 = FUN_00afe6c0(param_1,param_2,param_3,0x3d,0);
                    /* catch() { ... } // from try @ 00aff47c with catch @ 00affa8c */
    iVar1 = ((100 - iVar2) * iVar1) / 100;
  }
  return iVar1;
}

~~~
