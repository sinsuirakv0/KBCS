# 00c1ffdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00c1ffdc",
  "name": "FUN_00c1ffdc",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "afcbfce993581fe1f346912f33a8c17e952282bd2df36d8f9a691596a07b500c",
  "source_text_sha256": "afcbfce993581fe1f346912f33a8c17e952282bd2df36d8f9a691596a07b500c"
}
~~~

## 呼び出し元

- [00c1f064](../00c1f/00c1f064.md)
- [00c21500](../00c21/00c21500.md)

## 呼び出し先

- [00c3561c](../00c35/00c3561c.md)
- [00c538b0](../00c53/00c538b0.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c5dae0](../00c5d/00c5dae0.md)

## 疑似コード / UTF-8 1435 bytes

~~~c

void FUN_00c1ffdc(long param_1,long param_2)

{
  undefined *puVar1;
  ulong uVar2;
  long lVar3;
  ulong uVar4;
  long *plVar5;
  long *plVar6;
  ulong uVar7;
  undefined *local_48;
  undefined8 **local_40;
  undefined **local_38;
  
  puVar1 = PTR__ZNSt6__ndk17codecvtIDic9mbstate_tE2idE_00c9b838;
  local_48 = PTR__ZNSt6__ndk17codecvtIDic9mbstate_tE2idE_00c9b838;
  if (*(long *)PTR__ZNSt6__ndk17codecvtIDic9mbstate_tE2idE_00c9b838 != -1) {
    local_38 = &local_48;
    local_40 = &local_38;
                    /* try { // try from 00c20020 to 00d20027 has its CatchHandler @ 00c286c0 */
    _ZNSt6__ndk111__call_onceERVmPvPFvS2_E
              (PTR__ZNSt6__ndk17codecvtIDic9mbstate_tE2idE_00c9b838,&local_40,FUN_00c35b90);
  }
  uVar2 = (ulong)*(int *)(puVar1 + 8);
  uVar7 = uVar2 - 1;
  FUN_00c538b0(1,param_2 + 8);
  plVar5 = (long *)(param_1 + 0x10);
  lVar3 = *plVar5;
  uVar4 = *(long *)(param_1 + 0x18) - lVar3 >> 3;
  if (uVar4 <= uVar7) {
    if (uVar2 < uVar4 || uVar2 - uVar4 == 0) {
      if (uVar2 < uVar4) {
        *(ulong *)(param_1 + 0x18) = lVar3 + uVar2 * 8;
      }
    }
    else {
      FUN_00c3561c(plVar5,uVar2 - uVar4);
      lVar3 = *plVar5;
    }
  }
  plVar6 = *(long **)(lVar3 + uVar7 * 8);
  if ((plVar6 != (long *)0x0) && (lVar3 = FUN_00c538e0(0xffffffffffffffff,plVar6 + 1), lVar3 == 0))
  {
    (**(code **)(*plVar6 + 0x10))(plVar6);
  }
  *(long *)(*plVar5 + uVar7 * 8) = param_2;
  return;
}

~~~
