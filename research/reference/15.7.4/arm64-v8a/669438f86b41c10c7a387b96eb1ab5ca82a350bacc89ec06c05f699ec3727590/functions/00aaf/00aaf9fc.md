# 00aaf9fc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aaf9b8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf9b8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/inspection-0006.md#compare-9b9194fff41c412987f17f83c1433d34)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaf9fc",
  "name": "FUN_00aaf9fc",
  "size": 356,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0e02a54f546100577788137add3a420d0a72be8beab09181eb2be405df42388d",
  "source_text_sha256": "0e02a54f546100577788137add3a420d0a72be8beab09181eb2be405df42388d"
}
~~~

## 呼び出し元

- [00a2720c](../00a27/00a2720c.md)
- [00aafb60](../00aaf/00aafb60.md)

## 呼び出し先

- [0041fdf0](../0041f/0041fdf0.md)
- [00ab0e7c](../00ab0/00ab0e7c.md)
- [00bd70ec](../00bd7/00bd70ec.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb1b0](../00bdb/00bdb1b0.md)

## 関連文字列（未確認候補）

~~~text
"map::at:  key not found"
~~~

## 疑似コード / UTF-8 2655 bytes

~~~c

void FUN_00aaf9fc(long *param_1,long param_2)

{
  long *plVar1;
  void *__dest;
  undefined8 uVar2;
  long *plVar3;
  long lVar4;
  void *pvVar5;
  long *plVar6;
  long *plVar7;
  size_t __n;
  
  plVar1 = (long *)(param_2 + 8);
  plVar6 = (long *)*plVar1;
  plVar3 = plVar1;
  plVar7 = plVar6;
  if (plVar6 != (long *)0x0) {
    do {
      if (-1 < (int)*(uint *)(plVar7 + 4)) {
        plVar3 = plVar7;
      }
      plVar7 = *(long **)((long)plVar7 + ((ulong)(*(uint *)(plVar7 + 4) >> 0x1c) & 8));
    } while (plVar7 != (long *)0x0);
    if ((plVar3 == plVar1) || (0 < (int)plVar3[4])) {
      do {
        while (0 < (int)plVar6[4]) {
          plVar6 = (long *)*plVar6;
          if (plVar6 == (long *)0x0) goto LAB_00aafa98;
        }
        if (-1 < (int)plVar6[4]) {
          lVar4 = plVar6[5];
          param_1[2] = 0;
          param_1[3] = 0;
          param_1[1] = 0;
          *param_1 = lVar4;
          pvVar5 = (void *)plVar6[6];
          __n = plVar6[7] - (long)pvVar5;
          if (__n == 0) {
            return;
          }
          if (-1 < (long)__n) {
            __dest = (void *)_Znwm(__n);
            goto LAB_00aafb00;
          }
          FUN_00ab0e7c(param_1 + 1);
          goto LAB_00aafb34;
        }
        plVar6 = (long *)plVar6[1];
      } while (plVar6 != (long *)0x0);
    }
    else {
      do {
        while (0 < (int)plVar6[4]) {
          plVar6 = (long *)*plVar6;
          if (plVar6 == (long *)0x0) goto LAB_00aafa98;
        }
        if (-1 < (int)plVar6[4]) {
          lVar4 = plVar6[5];
          param_1[2] = 0;
          param_1[3] = 0;
          param_1[1] = 0;
          *param_1 = lVar4;
          pvVar5 = (void *)plVar6[6];
          __n = plVar6[7] - (long)pvVar5;
          if (__n != 0) {
            if ((long)__n < 0) {
LAB_00aafb34:
              uVar2 = FUN_00ab0e7c(param_1 + 1);
              pvVar5 = (void *)param_1[1];
              if (pvVar5 != (void *)0x0) {
                param_1[2] = (long)pvVar5;
                _ZdlPv(pvVar5);
              }
                    /* WARNING: Subroutine does not return */
              FUN_00bd70ec(uVar2);
            }
            __dest = (void *)_Znwm(__n);
LAB_00aafb00:
            param_1[1] = (long)__dest;
            param_1[2] = (long)__dest;
            param_1[3] = (long)__dest + __n;
            memcpy(__dest,pvVar5,__n);
            param_1[2] = (long)__dest + __n;
          }
          return;
        }
        plVar6 = (long *)plVar6[1];
      } while (plVar6 != (long *)0x0);
    }
  }
LAB_00aafa98:
                    /* WARNING: Subroutine does not return */
  FUN_0041fdf0("map::at:  key not found");
}

~~~
