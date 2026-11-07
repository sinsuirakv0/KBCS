# 00b4eecc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00b4edc0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4edc0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00b4eecc",
  "name": "_ZNK8firebase9messaging8internal13MessageReader14ReadFromBufferERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE",
  "size": 556,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c9595b1a9938848526ac25a764e58c2e2e5fbfaac9c9899a4ba2acf9f6e462d2",
  "source_text_sha256": "c9595b1a9938848526ac25a764e58c2e2e5fbfaac9c9899a4ba2acf9f6e462d2"
}
~~~

## 呼び出し元

- [00be0560](../00be0/00be0560.md)

## 呼び出し先

- [00bdb090](../00bdb/00bdb090.md)
- [00bdde40](../00bdd/00bdde40.md)
- [00be0500](../00be0/00be0500.md)
- [00be0550](../00be0/00be0550.md)

## 関連文字列（未確認候補）

~~~text
"%s Failed to load FCM messages, some messages may have been dropped! This may be due to, (1) the device being out of space, (2) a crash on a previous run of the application, (3) a change in internal serialization format following an upgrade."
"Detected invalid FCM event type."
"Detected malformed FCM event header."
"Detected premature end of a FCM message buffer."
"FCM buffer verification failed."
~~~

## 疑似コード / UTF-8 5927 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void _ZNK8firebase9messaging8internal13MessageReader14ReadFromBufferERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE
               (long param_1,byte *param_2)

{
  int *piVar1;
  undefined1 *puVar2;
  uint uVar3;
  byte bVar4;
  char cVar5;
  ulong uVar6;
  long lVar7;
  undefined8 uVar8;
  undefined8 uVar9;
  ulong uVar10;
  long lVar11;
  char *pcVar12;
  uint *puVar13;
  ushort *puVar14;
  uint *puVar15;
  ulong uVar16;
  uint *local_98;
  ulong uStack_90;
  undefined8 local_88;
  undefined8 uStack_80;
  undefined8 local_78;
  undefined1 local_70;
  long local_68;
  
  uVar9 = _UNK_002b1c18;
  uVar8 = _DAT_002b1c10;
                    /* try { // try from 00b4eee0 to 00c4eefb has its CatchHandler @ 00b4f410 */
  lVar7 = tpidr_el0;
  local_68 = *(long *)(lVar7 + 0x28);
  bVar4 = *param_2;
                    /* try { // try from 00b4eefc to 00c4ef47 has its CatchHandler @ 00b4f478 */
  uVar6 = (ulong)(bVar4 >> 1);
  if ((bVar4 & 1) != 0) {
    uVar6 = *(ulong *)(param_2 + 8);
  }
  if (uVar6 != 0) {
    puVar13 = *(uint **)(param_2 + 0x10);
    if ((bVar4 & 1) == 0) {
      puVar13 = (uint *)(param_2 + 1);
    }
                    /* try { // try from 00b4ef48 to 00c4ef9b has its CatchHandler @ 00b4ec84 */
    uVar10 = uVar6 - 4;
    if (3 < uVar6 && uVar10 != 0) {
      do {
        puVar15 = puVar13 + 1;
        uVar16 = (ulong)(int)*puVar13;
        uVar6 = uVar10 - uVar16;
        if (uVar10 < uVar16) {
                    /* try { // try from 00b4f0bc to 00c4f0c7 has its CatchHandler @ 00b4f278 */
          pcVar12 = "Detected malformed FCM event header.";
          goto LAB_00b4f0c0;
        }
        local_78 = 0;
        uStack_80 = uVar9;
        local_88 = uVar8;
        local_70 = 1;
        local_98 = puVar15;
        uStack_90 = uVar16;
                    /* try { // try from 00b4ef9c to 00c4efa7 has its CatchHandler @ 00b4f338 */
        if ((((*puVar13 < 5) || (uVar3 = *puVar15, (int)uVar3 < 1)) || (uVar16 - 1 < (ulong)uVar3))
           || (uVar10 = _ZNK3com6google8firebase9messaging3cpp15SerializedEvent6VerifyERN11flatbuffers8VerifierE
                                  ((long)puVar15 + (ulong)uVar3,&local_98), (uVar10 & 1) == 0)) {
          pcVar12 = "FCM buffer verification failed.";
                    /* try { // try from 00b4f098 to 00c4f0a3 has its CatchHandler @ 00b4f290 */
          goto LAB_00b4f0c0;
        }
                    /* try { // try from 00b4efc0 to 00c4efcb has its CatchHandler @ 00b4f334 */
        piVar1 = (int *)((long)puVar15 + (ulong)*puVar15);
        puVar13 = (uint *)((long)puVar15 + uVar16);
        puVar14 = (ushort *)((long)piVar1 - (long)*piVar1);
                    /* try { // try from 00b4efd4 to 00c4efdf has its CatchHandler @ 00b4f32c */
                    /* try { // try from 00b4efe0 to 00c4efeb has its CatchHandler @ 00b4f31c */
        if ((*puVar14 < 5) || ((ulong)puVar14[2] == 0)) {
LAB_00b4ef54:
          _ZN8firebase8LogErrorEPKcz
                    ("%s Failed to load FCM messages, some messages may have been dropped! This may be due to, (1) the device being out of space, (2) a crash on a previous run of the application, (3) a change in internal serialization format following an upgrade."
                     ,"Detected invalid FCM event type.");
        }
        else {
          cVar5 = *(char *)((long)piVar1 + (ulong)puVar14[2]);
          if (cVar5 == '\x02') {
            piVar1 = (int *)((long)((long)piVar1 + (ulong)puVar14[3]) +
                            (ulong)*(uint *)((long)piVar1 + (ulong)puVar14[3]));
                    /* try { // try from 00b4f02c to 00c4f037 has its CatchHandler @ 00b4f2c4 */
            if ((*(ushort *)((long)piVar1 - (long)*piVar1) < 5) ||
               (uVar10 = (ulong)((ushort *)((long)piVar1 - (long)*piVar1))[2], uVar10 == 0)) {
              lVar11 = 0;
            }
            else {
              puVar15 = (uint *)((long)piVar1 + uVar10);
              lVar11 = (long)puVar15 + (ulong)*puVar15;
                    /* try { // try from 00b4f050 to 00c4f05b has its CatchHandler @ 00b4f2c0 */
            }
            puVar2 = &DAT_002967d9;
            if (lVar11 != 0) {
              puVar2 = (undefined1 *)(lVar11 + 4);
            }
            (**(code **)(param_1 + 0x10))(puVar2,*(undefined8 *)(param_1 + 0x18));
                    /* try { // try from 00b4f080 to 00c4f097 has its CatchHandler @ 00b4f2a8 */
          }
          else {
            if (cVar5 != '\x01') goto LAB_00b4ef54;
                    /* try { // try from 00b4f004 to 00c4f00f has its CatchHandler @ 00b4f2d0 */
            if ((*puVar14 < 7) || ((ulong)puVar14[3] == 0)) {
              lVar11 = 0;
            }
            else {
              puVar15 = (uint *)((long)piVar1 + (ulong)puVar14[3]);
              lVar11 = (long)puVar15 + (ulong)*puVar15;
            }
            _ZNK8firebase9messaging8internal13MessageReader14ConsumeMessageEPKN3com6google8firebase9messaging3cpp17SerializedMessageE
                      (param_1,lVar11);
          }
        }
        if (uVar6 == 0) goto LAB_00b4f0c4;
        uVar10 = uVar6 - 4;
      } while (3 < uVar6 && uVar10 != 0);
    }
    pcVar12 = "Detected premature end of a FCM message buffer.";
LAB_00b4f0c0:
    _ZN8firebase8LogErrorEPKcz
              ("%s Failed to load FCM messages, some messages may have been dropped! This may be due to, (1) the device being out of space, (2) a crash on a previous run of the application, (3) a change in internal serialization format following an upgrade."
               ,pcVar12);
  }
LAB_00b4f0c4:
  if (*(long *)(lVar7 + 0x28) == local_68) {
                    /* try { // try from 00b4f0e4 to 00c4f0ef has its CatchHandler @ 00b4f26c */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
