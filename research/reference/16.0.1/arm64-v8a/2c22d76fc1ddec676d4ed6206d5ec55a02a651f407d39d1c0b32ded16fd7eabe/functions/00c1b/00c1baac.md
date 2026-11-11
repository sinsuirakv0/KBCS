# 00c1baac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00c1baac",
  "name": "_ZNSt6__ndk111__money_putIcE13__gather_infoEbbRKNS_6localeERNS_10money_base7patternERcS8_RNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEESF_SF_Ri",
  "size": 532,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6ced324615398db8ce2e96dbd947e1dc3f0d04cfb2fc25e4396eb1085049d7cc",
  "source_text_sha256": "6ced324615398db8ce2e96dbd947e1dc3f0d04cfb2fc25e4396eb1085049d7cc"
}
~~~

## 呼び出し元

- [00c5e6e0](../00c5e/00c5e6e0.md)

## 呼び出し先

- [00c05f58](../00c05/00c05f58.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c5dee0](../00c5d/00c5dee0.md)

## 疑似コード / UTF-8 3602 bytes

~~~c

void _ZNSt6__ndk111__money_putIcE13__gather_infoEbbRKNS_6localeERNS_10money_base7patternERcS8_RNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEESF_SF_Ri
               (ulong param_1,ulong param_2,long *param_3,undefined4 *param_4,undefined1 *param_5,
               undefined1 *param_6,byte *param_7,byte *param_8,byte *param_9,undefined4 *param_10)

{
  undefined *puVar1;
  undefined1 uVar2;
  undefined4 uVar3;
  long lVar4;
  code *pcVar5;
  long lVar6;
  long *plVar7;
  undefined **local_80;
  undefined8 uStack_78;
  undefined8 local_70;
  undefined *local_68;
  undefined ***local_48;
  
                    /* try { // try from 00c1babc to 00d1bacf has its CatchHandler @ 00c1d0ec */
  lVar6 = *param_3;
  if ((param_1 & 1) == 0) {
    lVar4 = *(long *)PTR__ZNSt6__ndk110moneypunctIcLb0EE2idE_00c9bbe0;
    puVar1 = PTR__ZNSt6__ndk110moneypunctIcLb0EE2idE_00c9bbe0;
  }
  else {
    lVar4 = *(long *)PTR__ZNSt6__ndk110moneypunctIcLb1EE2idE_00c9bbd8;
    puVar1 = PTR__ZNSt6__ndk110moneypunctIcLb1EE2idE_00c9bbd8;
  }
  local_68 = puVar1;
  if (lVar4 != -1) {
    local_48 = &local_80;
    local_80 = &local_68;
    _ZNSt6__ndk111__call_onceERVmPvPFvS2_E(puVar1,&local_48,FUN_00c35fb8);
  }
  lVar4 = *(long *)(lVar6 + 0x10);
  if (((long)*(int *)(puVar1 + 8) - 1U < (ulong)(*(long *)(lVar6 + 0x18) - lVar4 >> 3)) &&
     (plVar7 = *(long **)(lVar4 + ((long)*(int *)(puVar1 + 8) - 1U) * 8), plVar7 != (long *)0x0)) {
    if ((param_2 & 1) == 0) {
                    /* try { // try from 00c1bbb4 to 00d1bbbb has its CatchHandler @ 00c1d1e4 */
      uVar3 = (**(code **)(*plVar7 + 0x50))(plVar7);
      *param_4 = uVar3;
                    /* try { // try from 00c1bbbc to 00d1bbc3 has its CatchHandler @ 00c1d0e8 */
      pcVar5 = *(code **)(*plVar7 + 0x38);
    }
    else {
                    /* try { // try from 00c1bb90 to 00d1bb9f has its CatchHandler @ 00c1d2e8 */
      uVar3 = (**(code **)(*plVar7 + 0x58))(plVar7);
      *param_4 = uVar3;
      pcVar5 = *(code **)(*plVar7 + 0x40);
    }
    (*pcVar5)(&local_80,plVar7);
    if ((*param_9 & 1) != 0) {
      _ZdlPv(*(void **)(param_9 + 0x10));
    }
    *(undefined8 *)(param_9 + 8) = uStack_78;
    *(undefined ***)param_9 = local_80;
    *(undefined8 *)(param_9 + 0x10) = local_70;
    uVar2 = (**(code **)(*plVar7 + 0x18))(plVar7);
                    /* try { // try from 00c1bc00 to 00d1bc0b has its CatchHandler @ 00c1d0e4 */
    *param_5 = uVar2;
                    /* try { // try from 00c1bc0c to 00d1bc1b has its CatchHandler @ 00c1d0d0 */
    uVar2 = (**(code **)(*plVar7 + 0x20))(plVar7);
    *param_6 = uVar2;
                    /* try { // try from 00c1bc1c to 00d1bc2f has its CatchHandler @ 00c1d0b8 */
    (**(code **)(*plVar7 + 0x28))(&local_80,plVar7);
    if ((*param_7 & 1) != 0) {
      _ZdlPv(*(void **)(param_7 + 0x10));
    }
    *(undefined8 *)(param_7 + 8) = uStack_78;
    *(undefined ***)param_7 = local_80;
    *(undefined8 *)(param_7 + 0x10) = local_70;
    (**(code **)(*plVar7 + 0x30))(&local_80,plVar7);
    if ((*param_8 & 1) != 0) {
                    /* try { // try from 00c1bc68 to 00d1bc73 has its CatchHandler @ 00c1d1e4 */
      _ZdlPv(*(void **)(param_8 + 0x10));
    }
                    /* try { // try from 00c1bc74 to 00d1bd4f has its CatchHandler @ 00c1d198 */
    *(undefined8 *)(param_8 + 8) = uStack_78;
    *(undefined ***)param_8 = local_80;
    *(undefined8 *)(param_8 + 0x10) = local_70;
    uVar3 = (**(code **)(*plVar7 + 0x48))(plVar7);
    *param_10 = uVar3;
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_00c05f58();
}

~~~
