# 00aebdb8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/review-0014.md#review-7aa544ba0c61f53466d809289f847e7d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebdb8",
  "name": "FUN_00aebdb8",
  "size": 204,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ebd3e7e2221ab26b57a973964953e92bf1c6bc5505b99593ce4d2e7aad65ce85",
  "source_text_sha256": "ebd3e7e2221ab26b57a973964953e92bf1c6bc5505b99593ce4d2e7aad65ce85"
}
~~~

## 呼び出し元

- [00adf01c](../00adf/00adf01c.md)

## 呼び出し先

- [0043bb64](../0043b/0043bb64.md)
- [00c57a90](../00c57/00c57a90.md)

## 疑似コード / UTF-8 2908 bytes

~~~c

long * FUN_00aebdb8(long *param_1,int *param_2)

{
  int iVar1;
  long *plVar2;
  long *plVar3;
  long *plVar4;
  long *plVar5;
  
                    /* catch() { ... } // from try @ 00aeb3d4 with catch @ 00aebdc4 */
  iVar1 = *param_2;
  plVar4 = param_1 + 1;
                    /* catch() { ... } // from try @ 00aeb554 with catch @ 00aebddc */
  plVar3 = (long *)*plVar4;
  plVar5 = plVar4;
  if ((long *)*plVar4 != (long *)0x0) {
    do {
                    /* catch() { ... } // from try @ 00aeb458 with catch @ 00aebdf4 */
      while (plVar2 = plVar3, plVar4 = plVar2, iVar1 < (int)plVar2[4]) {
                    /* catch() { ... } // from try @ 00aeb4ec with catch @ 00aebdec */
        plVar3 = (long *)*plVar2;
        plVar5 = plVar2;
        if ((long *)*plVar2 == (long *)0x0) goto LAB_00aebe18;
      }
                    /* catch() { ... } // from try @ 00aeb3c4 with catch @ 00aebe04 */
      if (iVar1 <= (int)plVar2[4]) goto LAB_00aebe6c;
      plVar3 = (long *)plVar2[1];
    } while ((long *)plVar2[1] != (long *)0x0);
                    /* catch() { ... } // from try @ 00aeb6d0 with catch @ 00aebe14 */
    plVar5 = plVar2 + 1;
  }
LAB_00aebe18:
                    /* catch() { ... } // from try @ 00aeb4fc with catch @ 00aebe18 */
  plVar2 = (long *)_Znwm(0x40);
  plVar2[6] = 0;
  plVar2[7] = 0;
  plVar2[5] = 0;
  *plVar2 = 0;
  plVar2[1] = 0;
                    /* catch() { ... } // from try @ 00aebbc0 with catch @ 00aebe38 */
  plVar2[2] = (long)plVar4;
                    /* catch() { ... } // from try @ 00aebb58 with catch @ 00aebe3c */
  *plVar5 = (long)plVar2;
                    /* catch() { ... } // from try @ 00aebaf4 with catch @ 00aebe40 */
  plVar4 = (long *)*param_1;
                    /* catch() { ... } // from try @ 00aeb348 with catch @ 00aebe44 */
  *(int *)(plVar2 + 4) = iVar1;
                    /* catch() { ... } // from try @ 00aeb274 with catch @ 00aebe48 */
  plVar3 = plVar2;
  if (*plVar4 != 0) {
                    /* catch() { ... } // from try @ 00aeb1ec with catch @ 00aebe50 */
    *param_1 = *plVar4;
                    /* catch() { ... } // from try @ 00aeb108 with catch @ 00aebe54 */
    plVar3 = (long *)*plVar5;
  }
                    /* catch() { ... } // from try @ 00aeb2b8 with catch @ 00aebe5c
                       catch() { ... } // from try @ 00aebc54 with catch @ 00aebe5c */
  FUN_0043bb64(param_1[1],plVar3);
                    /* catch() { ... } // from try @ 00aeb064 with catch @ 00aebe60 */
  param_1[2] = param_1[2] + 1;
LAB_00aebe6c:
                    /* catch() { ... } // from try @ 00aeaf8c with catch @ 00aebe74 */
                    /* catch() { ... } // from try @ 00aeb14c with catch @ 00aebe7c
                       catch() { ... } // from try @ 00aebc40 with catch @ 00aebe7c */
                    /* catch() { ... } // from try @ 00aeaf24 with catch @ 00aebe80 */
  return plVar2 + 5;
}

~~~
