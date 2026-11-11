# 00c1fcfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00c1fcfc",
  "name": "FUN_00c1fcfc",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7f96602729d47183da60b8363a8f154b582798c34e14b824b905b93055197216",
  "source_text_sha256": "7f96602729d47183da60b8363a8f154b582798c34e14b824b905b93055197216"
}
~~~

## 呼び出し元

- [00c1f48c](../00c1f/00c1f48c.md)
- [00c21928](../00c21/00c21928.md)

## 呼び出し先

- [00c35a44](../00c35/00c35a44.md)
- [00c53cd0](../00c53/00c53cd0.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c5dee0](../00c5d/00c5dee0.md)

## 疑似コード / UTF-8 1775 bytes

~~~c

void FUN_00c1fcfc(long param_1,long param_2)

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
  
  puVar1 = PTR__ZNSt6__ndk17collateIwE2idE_00c9bc08;
  local_48 = PTR__ZNSt6__ndk17collateIwE2idE_00c9bc08;
  if (*(long *)PTR__ZNSt6__ndk17collateIwE2idE_00c9bc08 != -1) {
    local_38 = &local_48;
    local_40 = &local_38;
    _ZNSt6__ndk111__call_onceERVmPvPFvS2_E
              (PTR__ZNSt6__ndk17collateIwE2idE_00c9bc08,&local_40,FUN_00c35fb8);
  }
  uVar2 = (ulong)*(int *)(puVar1 + 8);
  uVar7 = uVar2 - 1;
  FUN_00c53cd0(1,param_2 + 8);
  plVar5 = (long *)(param_1 + 0x10);
  lVar3 = *plVar5;
                    /* try { // try from 00c1fd7c to 00d1fd8f has its CatchHandler @ 00c286a0 */
  uVar4 = *(long *)(param_1 + 0x18) - lVar3 >> 3;
  if (uVar4 <= uVar7) {
    if (uVar2 < uVar4 || uVar2 - uVar4 == 0) {
      if (uVar2 < uVar4) {
                    /* try { // try from 00c1fda8 to 00d1fdb3 has its CatchHandler @ 00c282b0 */
        *(ulong *)(param_1 + 0x18) = lVar3 + uVar2 * 8;
      }
    }
    else {
      FUN_00c35a44(plVar5,uVar2 - uVar4);
      lVar3 = *plVar5;
    }
  }
  plVar6 = *(long **)(lVar3 + uVar7 * 8);
                    /* try { // try from 00c1fdb4 to 00d1fdbf has its CatchHandler @ 00c282a0 */
                    /* try { // try from 00c1fdc0 to 00d1fdcb has its CatchHandler @ 00c28290 */
  if ((plVar6 != (long *)0x0) && (lVar3 = FUN_00c53d00(0xffffffffffffffff,plVar6 + 1), lVar3 == 0))
  {
                    /* try { // try from 00c1fdcc to 00d1fe33 has its CatchHandler @ 00c1f428 */
    (**(code **)(*plVar6 + 0x10))(plVar6);
  }
  *(long *)(*plVar5 + uVar7 * 8) = param_2;
  return;
}

~~~
