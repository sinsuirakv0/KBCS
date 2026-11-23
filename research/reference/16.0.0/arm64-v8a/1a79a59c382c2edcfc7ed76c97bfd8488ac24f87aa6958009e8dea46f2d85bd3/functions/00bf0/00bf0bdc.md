# 00bf0bdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b74194`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74194.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/alignment_unresolved-0018.md#compare-36e880165397fc0409685d84684bacd7)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf0bdc",
  "name": "FUN_00bf0bdc",
  "size": 308,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9e2bc01d9c5124797aebb75c51676b5b72926918da20f3a041a0a40123b90cc1",
  "source_text_sha256": "9e2bc01d9c5124797aebb75c51676b5b72926918da20f3a041a0a40123b90cc1"
}
~~~

## 呼び出し元

- [00bf0ea4](../00bf0/00bf0ea4.md)

## 呼び出し先

- [0043b724](../0043b/0043b724.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57b40](../00c57/00c57b40.md)

## 疑似コード / UTF-8 1326 bytes

~~~c

void FUN_00bf0bdc(ulong *param_1,ulong param_2,ulong param_3,long param_4,size_t param_5,
                 long param_6,long param_7)

{
  ulong uVar1;
  size_t __n;
  void *__dest;
  byte *__src;
  ulong uVar2;
  
  if (param_3 <= -param_2 - 9) {
    __src = (byte *)param_1[2];
    if ((*param_1 & 1) == 0) {
      __src = (byte *)((long)param_1 + 1);
    }
    if (param_2 < 0x7ffffffffffffff3) {
      uVar1 = param_3 + param_2;
      if (param_3 + param_2 <= param_2 * 2) {
        uVar1 = param_2 * 2;
      }
      if (uVar1 < 0x17) {
        uVar2 = 0x17;
      }
      else {
        uVar2 = (uVar1 & 0xfffffffffffffff8) + 8;
        if ((uVar1 | 7) != 0x17) {
          uVar2 = uVar1 | 7;
        }
        uVar2 = uVar2 + 1;
      }
    }
    else {
      uVar2 = 0xfffffffffffffff7;
    }
    __dest = (void *)_Znwm(uVar2);
    if (param_5 != 0) {
      memmove(__dest,__src,param_5);
    }
    __n = param_4 - (param_6 + param_5);
    if (__n != 0) {
      memmove((void *)((long)__dest + param_7 + param_5),__src + param_6 + param_5,__n);
    }
    if (param_2 != 0x16) {
      _ZdlPv(__src);
    }
    *param_1 = uVar2 | 1;
    param_1[1] = (param_4 - param_6) + param_7;
    param_1[2] = (ulong)__dest;
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_0043b724(param_1);
}

~~~
