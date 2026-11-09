# 006dfbec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "006dfbec",
  "name": "FUN_006dfbec",
  "size": 412,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "84f30f9b495c15e7fbc73cab08e66f93bbac0d39beddf025884adb5d74d8b651",
  "source_text_sha256": "84f30f9b495c15e7fbc73cab08e66f93bbac0d39beddf025884adb5d74d8b651"
}
~~~

## 呼び出し元

- [006ea548](../006ea/006ea548.md)

## 呼び出し先

- [0043bb64](../0043b/0043bb64.md)
- [00800338](../00800/00800338.md)
- [00805cf4](../00805/00805cf4.md)
- [008514b8](../00851/008514b8.md)
- [0085c10c](../0085c/0085c10c.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c58050](../00c58/00c58050.md)

## 疑似コード / UTF-8 2393 bytes

~~~c

void FUN_006dfbec(long param_1)

{
  wchar_t *pwVar1;
  int iVar2;
  undefined4 uVar3;
  long lVar4;
  wchar_t *pwVar5;
  undefined8 uVar6;
  undefined8 *puVar7;
  undefined8 *puVar8;
  long *plVar9;
  wchar_t *pwVar10;
  undefined8 *puVar11;
  undefined8 *puVar12;
  
  lVar4 = FUN_008514b8();
  if (*(int *)(lVar4 + 0x44e36c) == -1) {
    pwVar5 = *(wchar_t **)(param_1 + 0x18);
    pwVar1 = *(wchar_t **)(param_1 + 0x20);
    lVar4 = FUN_008514b8();
    pwVar5 = wmemchr(pwVar5,*(wchar_t *)(lVar4 + 0x44e368),(long)pwVar1 - (long)pwVar5 >> 2);
    pwVar10 = *(wchar_t **)(param_1 + 0x20);
    if (pwVar5 != (wchar_t *)0x0) {
      pwVar1 = pwVar5;
    }
    lVar4 = FUN_008514b8();
    if (pwVar1 == pwVar10) {
      uVar3 = FUN_0085c10c(lVar4,1);
    }
    else {
      uVar3 = *(undefined4 *)(lVar4 + 0x44e368);
    }
    lVar4 = FUN_008514b8();
    *(undefined4 *)(lVar4 + 0x44e36c) = uVar3;
  }
  lVar4 = FUN_008514b8();
  iVar2 = *(int *)(lVar4 + 0x44e36c);
                    /* catch() { ... } // from try @ 006dfe78 with catch @ 006dfc9c */
  *(int *)(param_1 + 0x30) = iVar2;
  if (iVar2 != -1) {
    uVar6 = FUN_00800338();
    uVar6 = FUN_00805cf4(uVar6,*(int *)(param_1 + 0x30) % 1000);
    iVar2 = *(int *)(param_1 + 0x30);
    puVar11 = (undefined8 *)(param_1 + 0x58);
    puVar8 = (undefined8 *)*puVar11;
    puVar12 = puVar11;
    if ((undefined8 *)*puVar11 != (undefined8 *)0x0) {
      do {
        while (puVar7 = puVar8, puVar11 = puVar7, iVar2 < *(int *)(puVar7 + 4)) {
          puVar8 = (undefined8 *)*puVar7;
          puVar12 = puVar7;
          if ((undefined8 *)*puVar7 == (undefined8 *)0x0) goto LAB_006dfd1c;
        }
        if (iVar2 <= *(int *)(puVar7 + 4)) goto LAB_006dfd6c;
        puVar8 = (undefined8 *)puVar7[1];
      } while ((undefined8 *)puVar7[1] != (undefined8 *)0x0);
      puVar12 = puVar7 + 1;
    }
LAB_006dfd1c:
    puVar7 = (undefined8 *)_Znwm(0x30);
    *puVar7 = 0;
    puVar7[1] = 0;
    puVar7[2] = puVar11;
    *puVar12 = puVar7;
    plVar9 = *(long **)(param_1 + 0x50);
    *(int *)(puVar7 + 4) = iVar2;
    puVar7[5] = 0;
    puVar8 = puVar7;
    if (*plVar9 != 0) {
      *(long *)(param_1 + 0x50) = *plVar9;
      puVar8 = (undefined8 *)*puVar12;
    }
    FUN_0043bb64(*(undefined8 *)(param_1 + 0x58),puVar8);
    *(long *)(param_1 + 0x60) = *(long *)(param_1 + 0x60) + 1;
LAB_006dfd6c:
    puVar7[5] = uVar6;
  }
  return;
}

~~~
