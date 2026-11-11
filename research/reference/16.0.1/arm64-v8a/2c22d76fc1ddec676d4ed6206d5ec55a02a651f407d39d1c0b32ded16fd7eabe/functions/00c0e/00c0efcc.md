# 00c0efcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00c0efcc",
  "name": "FUN_00c0efcc",
  "size": 528,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ad9f9836e170316636939fa2098d5e2f889a0686176c9498eace4fa95fd89159",
  "source_text_sha256": "ad9f9836e170316636939fa2098d5e2f889a0686176c9498eace4fa95fd89159"
}
~~~

## 呼び出し元

- [00c0efbc](../00c0e/00c0efbc.md)

## 呼び出し先

- [00459668](../00459/00459668.md)
- [00c101a4](../00c10/00c101a4.md)
- [00c57e50](../00c57/00c57e50.md)
- [00c57e70](../00c57/00c57e70.md)
- [00c58270](../00c58/00c58270.md)
- [00c58290](../00c58/00c58290.md)
- [00c5d220](../00c5d/00c5d220.md)
- [00c5e5d0](../00c5e/00c5e5d0.md)

## 疑似コード / UTF-8 2362 bytes

~~~c

void FUN_00c0efcc(undefined8 param_1,undefined8 param_2,long param_3,undefined4 param_4,
                 undefined8 param_5,char *param_6)

{
  uint uVar1;
  int iVar2;
  char *pcVar3;
  char *pcVar4;
  char cVar5;
  undefined1 auStack_a0 [8];
  undefined8 local_98;
  undefined8 uStack_90;
  undefined1 auStack_85 [45];
  char local_58 [24];
  undefined8 local_28;
  
  uVar1 = *(uint *)(param_3 + 8);
  local_28 = 0x25;
  pcVar3 = (char *)((ulong)&local_28 | 1);
  if ((((uVar1 >> 0xb & 1) != 0) && ((uVar1 & 0x4a) != 8)) && ((uVar1 & 0x4a) != 0x40)) {
    pcVar3 = (char *)((ulong)&local_28 | 2);
    local_28 = 0x2b25;
  }
  pcVar4 = pcVar3;
  if ((uVar1 >> 9 & 1) != 0) {
    pcVar4 = pcVar3 + 1;
    *pcVar3 = '#';
  }
  cVar5 = *param_6;
  while (cVar5 != '\0') {
    param_6 = param_6 + 1;
    *pcVar4 = cVar5;
    pcVar4 = pcVar4 + 1;
    cVar5 = *param_6;
  }
  if ((uVar1 & 0x4a) == 0x40) {
    cVar5 = 'o';
  }
  else if ((uVar1 & 0x4a) == 8) {
    cVar5 = 'x';
                    /* catch() { ... } // from try @ 00c0f258 with catch @ 00c0f07c */
    if ((uVar1 & 0x4000) != 0) {
      cVar5 = 'X';
    }
  }
  else {
    cVar5 = 'd';
  }
  *pcVar4 = cVar5;
  if (((DAT_01127ca0 & 1) == 0) && (iVar2 = __cxa_guard_acquire(&DAT_01127ca0), iVar2 != 0)) {
    DAT_01127c98 = newlocale(0x1fbf,"C",(__locale_t)0x0);
                    /* try { // try from 00c0f1d0 to 00d0f257 has its CatchHandler @ 00c0f33c */
    __cxa_guard_release(&DAT_01127ca0);
  }
  iVar2 = FUN_00c101a4(local_58,0x18,DAT_01127c98,&local_28,param_5);
  uVar1 = *(uint *)(param_3 + 8) & 0xb0;
  pcVar3 = local_58 + iVar2;
  if (uVar1 == 0x20) goto LAB_00c0f13c;
  if (uVar1 == 0x10) {
    if ((local_58[0] == '-') || (local_58[0] == '+')) {
      pcVar3 = (char *)((ulong)local_58 | 1);
      goto LAB_00c0f13c;
    }
    if (((1 < iVar2) && (local_58[0] == '0')) && ((byte)(local_58[1] | 0x20U) == 0x78)) {
      pcVar3 = (char *)((ulong)local_58 | 2);
      goto LAB_00c0f13c;
    }
  }
  pcVar3 = local_58;
LAB_00c0f13c:
  _ZNKSt6__ndk18ios_base6getlocEv(auStack_a0,param_3);
  _ZNSt6__ndk19__num_putIcE21__widen_and_group_intEPcS2_S2_S2_RS2_S3_RKNS_6localeE
            (local_58,pcVar3,local_58 + iVar2,auStack_85,&uStack_90,&local_98,auStack_a0);
  _ZNSt6__ndk16localeD1Ev(auStack_a0);
  FUN_00459668(param_2,auStack_85,uStack_90,local_98,param_3,param_4);
  return;
}

~~~
