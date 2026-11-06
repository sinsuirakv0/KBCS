# 00af4cdc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00af4cdc.md)

## 関数情報

~~~json
{
  "address": "00af4cdc",
  "name": "_ZN8firebase4util18JIntArrayToVariantEP7_JNIEnvP10_jintArray",
  "size": 380,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "94647958ef482864a70dfd3b5f007f2a5a95589cb3d67b9e2d9f3927d575e0c4",
  "source_text_sha256": "94647958ef482864a70dfd3b5f007f2a5a95589cb3d67b9e2d9f3927d575e0c4"
}
~~~
## 呼び出し元

- [00bde530](../00bde/00bde530.md)

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdd9e0](../00bdd/00bdd9e0.md)
- [00bdd9f0](../00bdd/00bdd9f0.md)
- [00bde2c0](../00bde/00bde2c0.md)

## 疑似コード 1/1 / UTF-8 1883 bytes

~~~c

void _ZN8firebase4util18JIntArrayToVariantEP7_JNIEnvP10_jintArray
               (undefined4 *param_1,long *param_2,undefined8 param_3)

{
  undefined4 *puVar1;
  long lVar2;
  int iVar3;
  long lVar4;
  long *plVar5;
  undefined4 *puVar6;
  long lVar7;
  ulong uVar8;
  ulong uVar9;
  undefined4 local_80 [2];
  long local_78;
  long local_68;
  
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  iVar3 = (**(code **)(*param_2 + 0x558))();
  lVar4 = (**(code **)(*param_2 + 0x5d8))(param_2,param_3,0);
  plVar5 = (long *)_Znwm(0x18);
  plVar5[1] = 0;
  plVar5[2] = 0;
  *plVar5 = 0;
  if (iVar3 != 0) {
    uVar8 = (ulong)iVar3;
    if (iVar3 < 0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    puVar6 = (undefined4 *)_Znwm(uVar8 * 0x18);
    puVar1 = puVar6 + uVar8 * 6;
    *plVar5 = (long)puVar6;
    plVar5[1] = (long)puVar6;
    plVar5[2] = (long)puVar1;
    do {
      *puVar6 = 0;
      *(undefined8 *)(puVar6 + 2) = 0;
      puVar6 = puVar6 + 6;
    } while (puVar1 != puVar6);
    plVar5[1] = (long)puVar1;
    if (iVar3 != 0) {
      lVar7 = 0;
      uVar9 = 0;
      do {
        iVar3 = *(int *)(lVar4 + uVar9 * 4);
        local_80[0] = 0;
        _ZN8firebase7Variant5ClearENS0_4TypeE(local_80,1);
        local_78 = (long)iVar3;
        _ZN8firebase7VariantaSEOS0_(*plVar5 + lVar7,local_80);
        _ZN8firebase7Variant5ClearENS0_4TypeE(local_80,0);
        uVar9 = uVar9 + 1;
        lVar7 = lVar7 + 0x18;
      } while (uVar9 < uVar8);
    }
  }
  *param_1 = 0;
  *(undefined8 *)(param_1 + 2) = 0;
  _ZN8firebase7Variant5ClearENS0_4TypeE(param_1,0);
  *param_1 = 6;
  *(long **)(param_1 + 2) = plVar5;
  (**(code **)(*param_2 + 0x618))(param_2,param_3,lVar4,2);
  if (*(long *)(lVar2 + 0x28) == local_68) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
