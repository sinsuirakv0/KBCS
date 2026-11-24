# 00b4eecc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b4ee88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ee88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0009.md#compare-ca4a0e34247eb24fa6930f6b7189b334)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bbd30c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbd/00bbd30c.md) · 移動量 `+0x6e440`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0064.md#compare-e1b1a6837869f807c3f2f47c8647ae04)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_text_sha256": "c9595b1a9938848526ac25a764e58c2e2e5fbfaac9c9899a4ba2acf9f6e462d2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4eecc",
        "00b4f0f7"
      ]
    ],
    "bytes_sha256": "88af4f18a2e266c4c705b76b2b7d901d0e43a688e1f7fa017694cb40a22f748a",
    "instruction_count": 139,
    "instruction_bytes": 556,
    "body_bytes": 556,
    "indirect": 1,
    "unresolved": 1
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4eecc"></a> `00b4eecc` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00b4eed0"></a> `00b4eed0` | `fb 2b 00 f9` | str x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b4eed4"></a> `00b4eed4` | `fa 67 06 a9` | stp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b4eed8"></a> `00b4eed8` | `f8 5f 07 a9` | stp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b4eedc"></a> `00b4eedc` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00b4eee0"></a> `00b4eee0` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b4eee4"></a> `00b4eee4` | `fd 7b 0a a9` | stp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00b4eee8"></a> `00b4eee8` | `fd 83 02 91` | add x29,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00b4eeec"></a> `00b4eeec` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b4eef0"></a> `00b4eef0` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00b4eef4"></a> `00b4eef4` | `e8 27 00 f9` | str x8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00b4eef8"></a> `00b4eef8` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00b4eefc"></a> `00b4eefc` | `29 04 40 f9` | ldr x9,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00b4ef00"></a> `00b4ef00` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b4ef04"></a> `00b4ef04` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b4ef08"></a> `00b4ef08` | `57 01 89 9a` | csel x23,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00b4ef0c"></a> `00b4ef0c` | `d7 0d 00 b4` | cbz x23,0x00b4f0c4 | `CONDITIONAL_JUMP`
<a id="insn-00b4ef10"></a> `00b4ef10` | `29 08 40 f9` | ldr x9,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00b4ef14"></a> `00b4ef14` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b4ef18"></a> `00b4ef18` | `08 bb ff f0` | adrp x8,0x2b1000 | `FALL_THROUGH`
<a id="insn-00b4ef1c"></a> `00b4ef1c` | `00 05 c3 3d` | ldr q0,[x8, #0xc10] | `FALL_THROUGH`
<a id="insn-00b4ef20"></a> `00b4ef20` | `59 ba ff 90` | adrp x25,0x296000 | `FALL_THROUGH`
<a id="insn-00b4ef24"></a> `00b4ef24` | `54 bd ff d0` | adrp x20,0x2f8000 | `FALL_THROUGH`
<a id="insn-00b4ef28"></a> `00b4ef28` | `95 ba ff d0` | adrp x21,0x2a0000 | `FALL_THROUGH`
<a id="insn-00b4ef2c"></a> `00b4ef2c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b4ef30"></a> `00b4ef30` | `38 00 80 52` | mov w24,#0x1 | `FALL_THROUGH`
<a id="insn-00b4ef34"></a> `00b4ef34` | `39 67 1f 91` | add x25,x25,#0x7d9 | `FALL_THROUGH`
<a id="insn-00b4ef38"></a> `00b4ef38` | `94 62 29 91` | add x20,x20,#0xa58 | `FALL_THROUGH`
<a id="insn-00b4ef3c"></a> `00b4ef3c` | `3a 15 81 9a` | csinc x26,x9,x1,ne | `FALL_THROUGH`
<a id="insn-00b4ef40"></a> `00b4ef40` | `b5 f2 06 91` | add x21,x21,#0x1bc | `FALL_THROUGH`
<a id="insn-00b4ef44"></a> `00b4ef44` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-00b4ef48"></a> `00b4ef48` | `e8 12 00 f1` | subs x8,x23,#0x4 | `FALL_THROUGH`
<a id="insn-00b4ef4c"></a> `00b4ef4c` | `08 01 00 54` | b.hi 0x00b4ef6c | `CONDITIONAL_JUMP`
<a id="insn-00b4ef50"></a> `00b4ef50` | `53 00 00 14` | b 0x00b4f09c | `UNCONDITIONAL_JUMP`
<a id="insn-00b4ef54"></a> `00b4ef54` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b4ef58"></a> `00b4ef58` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b4ef5c"></a> `00b4ef5c` | `b9 3b 02 94` | bl 0x00bdde40 | `UNCONDITIONAL_CALL`
<a id="insn-00b4ef60"></a> `00b4ef60` | `37 0b 00 b4` | cbz x23,0x00b4f0c4 | `CONDITIONAL_JUMP`
<a id="insn-00b4ef64"></a> `00b4ef64` | `e8 12 00 f1` | subs x8,x23,#0x4 | `FALL_THROUGH`
<a id="insn-00b4ef68"></a> `00b4ef68` | `a9 09 00 54` | b.ls 0x00b4f09c | `CONDITIONAL_JUMP`
<a id="insn-00b4ef6c"></a> `00b4ef6c` | `5b 47 80 b8` | ldrsw x27,[x26], #0x4 | `FALL_THROUGH`
<a id="insn-00b4ef70"></a> `00b4ef70` | `17 01 1b eb` | subs x23,x8,x27 | `FALL_THROUGH`
<a id="insn-00b4ef74"></a> `00b4ef74` | `e3 09 00 54` | b.cc 0x00b4f0b0 | `CONDITIONAL_JUMP`
<a id="insn-00b4ef78"></a> `00b4ef78` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00b4ef7c"></a> `00b4ef7c` | `7f 17 00 71` | cmp w27,#0x5 | `FALL_THROUGH`
<a id="insn-00b4ef80"></a> `00b4ef80` | `fa ef 01 a9` | stp x26,x27,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b4ef84"></a> `00b4ef84` | `ff 1f 00 f9` | str xzr,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00b4ef88"></a> `00b4ef88` | `e0 83 82 3c` | stur q0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b4ef8c"></a> `00b4ef8c` | `f8 03 01 39` | strb w24,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b4ef90"></a> `00b4ef90` | `c3 07 00 54` | b.cc 0x00b4f088 | `CONDITIONAL_JUMP`
<a id="insn-00b4ef94"></a> `00b4ef94` | `48 03 40 b9` | ldr w8,[x26] | `FALL_THROUGH`
<a id="insn-00b4ef98"></a> `00b4ef98` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b4ef9c"></a> `00b4ef9c` | `6b 07 00 54` | b.lt 0x00b4f088 | `CONDITIONAL_JUMP`
<a id="insn-00b4efa0"></a> `00b4efa0` | `69 07 00 d1` | sub x9,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00b4efa4"></a> `00b4efa4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00b4efa8"></a> `00b4efa8` | `03 07 00 54` | b.cc 0x00b4f088 | `CONDITIONAL_JUMP`
<a id="insn-00b4efac"></a> `00b4efac` | `40 03 08 8b` | add x0,x26,x8 | `FALL_THROUGH`
<a id="insn-00b4efb0"></a> `00b4efb0` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b4efb4"></a> `00b4efb4` | `53 45 02 94` | bl 0x00be0500 | `UNCONDITIONAL_CALL`
<a id="insn-00b4efb8"></a> `00b4efb8` | `80 06 00 36` | tbz w0,#0x0,0x00b4f088 | `CONDITIONAL_JUMP`
<a id="insn-00b4efbc"></a> `00b4efbc` | `48 03 40 b9` | ldr w8,[x26] | `FALL_THROUGH`
<a id="insn-00b4efc0"></a> `00b4efc0` | `48 03 08 8b` | add x8,x26,x8 | `FALL_THROUGH`
<a id="insn-00b4efc4"></a> `00b4efc4` | `09 01 80 b9` | ldrsw x9,[x8] | `FALL_THROUGH`
<a id="insn-00b4efc8"></a> `00b4efc8` | `5a 03 1b 8b` | add x26,x26,x27 | `FALL_THROUGH`
<a id="insn-00b4efcc"></a> `00b4efcc` | `09 01 09 cb` | sub x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4efd0"></a> `00b4efd0` | `2a 01 40 79` | ldrh w10,[x9] | `FALL_THROUGH`
<a id="insn-00b4efd4"></a> `00b4efd4` | `5f 15 00 71` | cmp w10,#0x5 | `FALL_THROUGH`
<a id="insn-00b4efd8"></a> `00b4efd8` | `e3 fb ff 54` | b.cc 0x00b4ef54 | `CONDITIONAL_JUMP`
<a id="insn-00b4efdc"></a> `00b4efdc` | `2b 09 40 79` | ldrh w11,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00b4efe0"></a> `00b4efe0` | `ab fb ff b4` | cbz x11,0x00b4ef54 | `CONDITIONAL_JUMP`
<a id="insn-00b4efe4"></a> `00b4efe4` | `0b 69 6b 38` | ldrb w11,[x8, x11, LSL ] | `FALL_THROUGH`
<a id="insn-00b4efe8"></a> `00b4efe8` | `7f 09 00 71` | cmp w11,#0x2 | `FALL_THROUGH`
<a id="insn-00b4efec"></a> `00b4efec` | `60 01 00 54` | b.eq 0x00b4f018 | `CONDITIONAL_JUMP`
<a id="insn-00b4eff0"></a> `00b4eff0` | `7f 05 00 71` | cmp w11,#0x1 | `FALL_THROUGH`
<a id="insn-00b4eff4"></a> `00b4eff4` | `01 fb ff 54` | b.ne 0x00b4ef54 | `CONDITIONAL_JUMP`
<a id="insn-00b4eff8"></a> `00b4eff8` | `5f 1d 00 71` | cmp w10,#0x7 | `FALL_THROUGH`
<a id="insn-00b4effc"></a> `00b4effc` | `c3 02 00 54` | b.cc 0x00b4f054 | `CONDITIONAL_JUMP`
<a id="insn-00b4f000"></a> `00b4f000` | `29 0d 40 79` | ldrh w9,[x9, #0x6] | `FALL_THROUGH`
<a id="insn-00b4f004"></a> `00b4f004` | `89 02 00 b4` | cbz x9,0x00b4f054 | `CONDITIONAL_JUMP`
<a id="insn-00b4f008"></a> `00b4f008` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f00c"></a> `00b4f00c` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f010"></a> `00b4f010` | `01 01 09 8b` | add x1,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f014"></a> `00b4f014` | `11 00 00 14` | b 0x00b4f058 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f018"></a> `00b4f018` | `29 0d 40 79` | ldrh w9,[x9, #0x6] | `FALL_THROUGH`
<a id="insn-00b4f01c"></a> `00b4f01c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f020"></a> `00b4f020` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f024"></a> `00b4f024` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f028"></a> `00b4f028` | `09 01 80 b9` | ldrsw x9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f02c"></a> `00b4f02c` | `09 01 09 cb` | sub x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f030"></a> `00b4f030` | `2a 01 40 79` | ldrh w10,[x9] | `FALL_THROUGH`
<a id="insn-00b4f034"></a> `00b4f034` | `5f 15 00 71` | cmp w10,#0x5 | `FALL_THROUGH`
<a id="insn-00b4f038"></a> `00b4f038` | `83 01 00 54` | b.cc 0x00b4f068 | `CONDITIONAL_JUMP`
<a id="insn-00b4f03c"></a> `00b4f03c` | `29 09 40 79` | ldrh w9,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00b4f040"></a> `00b4f040` | `49 01 00 b4` | cbz x9,0x00b4f068 | `CONDITIONAL_JUMP`
<a id="insn-00b4f044"></a> `00b4f044` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f048"></a> `00b4f048` | `09 01 40 b9` | ldr w9,[x8] | `FALL_THROUGH`
<a id="insn-00b4f04c"></a> `00b4f04c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f050"></a> `00b4f050` | `07 00 00 14` | b 0x00b4f06c | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f054"></a> `00b4f054` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00b4f058"></a> `00b4f058` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4f05c"></a> `00b4f05c` | `3d 45 02 94` | bl 0x00be0550 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f060"></a> `00b4f060` | `37 f8 ff b5` | cbnz x23,0x00b4ef64 | `CONDITIONAL_JUMP`
<a id="insn-00b4f064"></a> `00b4f064` | `18 00 00 14` | b 0x00b4f0c4 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f068"></a> `00b4f068` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b4f06c"></a> `00b4f06c` | `69 06 41 a9` | ldp x9,x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b4f070"></a> `00b4f070` | `0a 11 00 91` | add x10,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00b4f074"></a> `00b4f074` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00b4f078"></a> `00b4f078` | `20 03 8a 9a` | csel x0,x25,x10,eq | `FALL_THROUGH`
<a id="insn-00b4f07c"></a> `00b4f07c` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00b4f080"></a> `00b4f080` | `37 f7 ff b5` | cbnz x23,0x00b4ef64 | `CONDITIONAL_JUMP`
<a id="insn-00b4f084"></a> `00b4f084` | `10 00 00 14` | b 0x00b4f0c4 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f088"></a> `00b4f088` | `40 bd ff b0` | adrp x0,0x2f8000 | `FALL_THROUGH`
<a id="insn-00b4f08c"></a> `00b4f08c` | `81 ba ff 90` | adrp x1,0x29f000 | `FALL_THROUGH`
<a id="insn-00b4f090"></a> `00b4f090` | `00 60 29 91` | add x0,x0,#0xa58 | `FALL_THROUGH`
<a id="insn-00b4f094"></a> `00b4f094` | `21 7c 02 91` | add x1,x1,#0x9f | `FALL_THROUGH`
<a id="insn-00b4f098"></a> `00b4f098` | `0a 00 00 14` | b 0x00b4f0c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f09c"></a> `00b4f09c` | `40 bd ff b0` | adrp x0,0x2f8000 | `FALL_THROUGH`
<a id="insn-00b4f0a0"></a> `00b4f0a0` | `21 ba ff 90` | adrp x1,0x293000 | `FALL_THROUGH`
<a id="insn-00b4f0a4"></a> `00b4f0a4` | `00 60 29 91` | add x0,x0,#0xa58 | `FALL_THROUGH`
<a id="insn-00b4f0a8"></a> `00b4f0a8` | `21 40 0e 91` | add x1,x1,#0x390 | `FALL_THROUGH`
<a id="insn-00b4f0ac"></a> `00b4f0ac` | `05 00 00 14` | b 0x00b4f0c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4f0b0"></a> `00b4f0b0` | `40 bd ff b0` | adrp x0,0x2f8000 | `FALL_THROUGH`
<a id="insn-00b4f0b4"></a> `00b4f0b4` | `e1 ba ff 90` | adrp x1,0x2ab000 | `FALL_THROUGH`
<a id="insn-00b4f0b8"></a> `00b4f0b8` | `00 60 29 91` | add x0,x0,#0xa58 | `FALL_THROUGH`
<a id="insn-00b4f0bc"></a> `00b4f0bc` | `21 a4 04 91` | add x1,x1,#0x129 | `FALL_THROUGH`
<a id="insn-00b4f0c0"></a> `00b4f0c0` | `60 3b 02 94` | bl 0x00bdde40 | `UNCONDITIONAL_CALL`
<a id="insn-00b4f0c4"></a> `00b4f0c4` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00b4f0c8"></a> `00b4f0c8` | `e9 27 40 f9` | ldr x9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00b4f0cc"></a> `00b4f0cc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b4f0d0"></a> `00b4f0d0` | `21 01 00 54` | b.ne 0x00b4f0f4 | `CONDITIONAL_JUMP`
<a id="insn-00b4f0d4"></a> `00b4f0d4` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00b4f0d8"></a> `00b4f0d8` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b4f0dc"></a> `00b4f0dc` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00b4f0e0"></a> `00b4f0e0` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b4f0e4"></a> `00b4f0e4` | `fa 67 46 a9` | ldp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b4f0e8"></a> `00b4f0e8` | `fb 2b 40 f9` | ldr x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b4f0ec"></a> `00b4f0ec` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00b4f0f0"></a> `00b4f0f0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b4f0f4"></a> `00b4f0f4` | `e7 2f 02 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4eecc`](#insn-00b4eecc) 範囲 `[['00b4eecc', '00b4eedf']]`
  - `FALL_THROUGH` [`00b4eedc`](#insn-00b4eedc) → [`00b4eee0`](#insn-00b4eee0)
- ブロック [`00b4eee0`](#insn-00b4eee0) 範囲 `[['00b4eee0', '00b4eefb']]`
  - `FALL_THROUGH` [`00b4eef8`](#insn-00b4eef8) → [`00b4eefc`](#insn-00b4eefc)
- ブロック [`00b4eefc`](#insn-00b4eefc) 範囲 `[['00b4eefc', '00b4ef0f']]`
  - `CONDITIONAL_JUMP` [`00b4ef0c`](#insn-00b4ef0c) → [`00b4f0c4`](#insn-00b4f0c4)
  - `FALL_THROUGH` [`00b4ef0c`](#insn-00b4ef0c) → [`00b4ef10`](#insn-00b4ef10)
- ブロック [`00b4ef10`](#insn-00b4ef10) 範囲 `[['00b4ef10', '00b4ef47']]`
  - `FALL_THROUGH` [`00b4ef44`](#insn-00b4ef44) → [`00b4ef48`](#insn-00b4ef48)
- ブロック [`00b4ef48`](#insn-00b4ef48) 範囲 `[['00b4ef48', '00b4ef4f']]`
  - `CONDITIONAL_JUMP` [`00b4ef4c`](#insn-00b4ef4c) → [`00b4ef6c`](#insn-00b4ef6c)
  - `FALL_THROUGH` [`00b4ef4c`](#insn-00b4ef4c) → [`00b4ef50`](#insn-00b4ef50)
- ブロック [`00b4ef50`](#insn-00b4ef50) 範囲 `[['00b4ef50', '00b4ef53']]`
  - `UNCONDITIONAL_JUMP` [`00b4ef50`](#insn-00b4ef50) → [`00b4f09c`](#insn-00b4f09c)
- ブロック [`00b4ef54`](#insn-00b4ef54) 範囲 `[['00b4ef54', '00b4ef63']]`
  - `CONDITIONAL_JUMP` [`00b4ef60`](#insn-00b4ef60) → [`00b4f0c4`](#insn-00b4f0c4)
  - `FALL_THROUGH` [`00b4ef60`](#insn-00b4ef60) → [`00b4ef64`](#insn-00b4ef64)
- ブロック [`00b4ef64`](#insn-00b4ef64) 範囲 `[['00b4ef64', '00b4ef6b']]`
  - `CONDITIONAL_JUMP` [`00b4ef68`](#insn-00b4ef68) → [`00b4f09c`](#insn-00b4f09c)
  - `FALL_THROUGH` [`00b4ef68`](#insn-00b4ef68) → [`00b4ef6c`](#insn-00b4ef6c)
- ブロック [`00b4ef6c`](#insn-00b4ef6c) 範囲 `[['00b4ef6c', '00b4ef77']]`
  - `CONDITIONAL_JUMP` [`00b4ef74`](#insn-00b4ef74) → [`00b4f0b0`](#insn-00b4f0b0)
  - `FALL_THROUGH` [`00b4ef74`](#insn-00b4ef74) → [`00b4ef78`](#insn-00b4ef78)
- ブロック [`00b4ef78`](#insn-00b4ef78) 範囲 `[['00b4ef78', '00b4ef93']]`
  - `CONDITIONAL_JUMP` [`00b4ef90`](#insn-00b4ef90) → [`00b4f088`](#insn-00b4f088)
  - `FALL_THROUGH` [`00b4ef90`](#insn-00b4ef90) → [`00b4ef94`](#insn-00b4ef94)
- ブロック [`00b4ef94`](#insn-00b4ef94) 範囲 `[['00b4ef94', '00b4ef9b']]`
  - `FALL_THROUGH` [`00b4ef98`](#insn-00b4ef98) → [`00b4ef9c`](#insn-00b4ef9c)
- ブロック [`00b4ef9c`](#insn-00b4ef9c) 範囲 `[['00b4ef9c', '00b4ef9f']]`
  - `CONDITIONAL_JUMP` [`00b4ef9c`](#insn-00b4ef9c) → [`00b4f088`](#insn-00b4f088)
  - `FALL_THROUGH` [`00b4ef9c`](#insn-00b4ef9c) → [`00b4efa0`](#insn-00b4efa0)
- ブロック [`00b4efa0`](#insn-00b4efa0) 範囲 `[['00b4efa0', '00b4efab']]`
  - `CONDITIONAL_JUMP` [`00b4efa8`](#insn-00b4efa8) → [`00b4f088`](#insn-00b4f088)
  - `FALL_THROUGH` [`00b4efa8`](#insn-00b4efa8) → [`00b4efac`](#insn-00b4efac)
- ブロック [`00b4efac`](#insn-00b4efac) 範囲 `[['00b4efac', '00b4efbb']]`
  - `CONDITIONAL_JUMP` [`00b4efb8`](#insn-00b4efb8) → [`00b4f088`](#insn-00b4f088)
  - `FALL_THROUGH` [`00b4efb8`](#insn-00b4efb8) → [`00b4efbc`](#insn-00b4efbc)
- ブロック [`00b4efbc`](#insn-00b4efbc) 範囲 `[['00b4efbc', '00b4efbf']]`
  - `FALL_THROUGH` [`00b4efbc`](#insn-00b4efbc) → [`00b4efc0`](#insn-00b4efc0)
- ブロック [`00b4efc0`](#insn-00b4efc0) 範囲 `[['00b4efc0', '00b4efd3']]`
  - `FALL_THROUGH` [`00b4efd0`](#insn-00b4efd0) → [`00b4efd4`](#insn-00b4efd4)
- ブロック [`00b4efd4`](#insn-00b4efd4) 範囲 `[['00b4efd4', '00b4efdb']]`
  - `CONDITIONAL_JUMP` [`00b4efd8`](#insn-00b4efd8) → [`00b4ef54`](#insn-00b4ef54)
  - `FALL_THROUGH` [`00b4efd8`](#insn-00b4efd8) → [`00b4efdc`](#insn-00b4efdc)
- ブロック [`00b4efdc`](#insn-00b4efdc) 範囲 `[['00b4efdc', '00b4efdf']]`
  - `FALL_THROUGH` [`00b4efdc`](#insn-00b4efdc) → [`00b4efe0`](#insn-00b4efe0)
- ブロック [`00b4efe0`](#insn-00b4efe0) 範囲 `[['00b4efe0', '00b4efe3']]`
  - `CONDITIONAL_JUMP` [`00b4efe0`](#insn-00b4efe0) → [`00b4ef54`](#insn-00b4ef54)
  - `FALL_THROUGH` [`00b4efe0`](#insn-00b4efe0) → [`00b4efe4`](#insn-00b4efe4)
- ブロック [`00b4efe4`](#insn-00b4efe4) 範囲 `[['00b4efe4', '00b4efef']]`
  - `CONDITIONAL_JUMP` [`00b4efec`](#insn-00b4efec) → [`00b4f018`](#insn-00b4f018)
  - `FALL_THROUGH` [`00b4efec`](#insn-00b4efec) → [`00b4eff0`](#insn-00b4eff0)
- ブロック [`00b4eff0`](#insn-00b4eff0) 範囲 `[['00b4eff0', '00b4eff7']]`
  - `CONDITIONAL_JUMP` [`00b4eff4`](#insn-00b4eff4) → [`00b4ef54`](#insn-00b4ef54)
  - `FALL_THROUGH` [`00b4eff4`](#insn-00b4eff4) → [`00b4eff8`](#insn-00b4eff8)
- ブロック [`00b4eff8`](#insn-00b4eff8) 範囲 `[['00b4eff8', '00b4efff']]`
  - `CONDITIONAL_JUMP` [`00b4effc`](#insn-00b4effc) → [`00b4f054`](#insn-00b4f054)
  - `FALL_THROUGH` [`00b4effc`](#insn-00b4effc) → [`00b4f000`](#insn-00b4f000)
- ブロック [`00b4f000`](#insn-00b4f000) 範囲 `[['00b4f000', '00b4f003']]`
  - `FALL_THROUGH` [`00b4f000`](#insn-00b4f000) → [`00b4f004`](#insn-00b4f004)
- ブロック [`00b4f004`](#insn-00b4f004) 範囲 `[['00b4f004', '00b4f007']]`
  - `CONDITIONAL_JUMP` [`00b4f004`](#insn-00b4f004) → [`00b4f054`](#insn-00b4f054)
  - `FALL_THROUGH` [`00b4f004`](#insn-00b4f004) → [`00b4f008`](#insn-00b4f008)
- ブロック [`00b4f008`](#insn-00b4f008) 範囲 `[['00b4f008', '00b4f017']]`
  - `UNCONDITIONAL_JUMP` [`00b4f014`](#insn-00b4f014) → [`00b4f058`](#insn-00b4f058)
- ブロック [`00b4f018`](#insn-00b4f018) 範囲 `[['00b4f018', '00b4f02b']]`
  - `FALL_THROUGH` [`00b4f028`](#insn-00b4f028) → [`00b4f02c`](#insn-00b4f02c)
- ブロック [`00b4f02c`](#insn-00b4f02c) 範囲 `[['00b4f02c', '00b4f03b']]`
  - `CONDITIONAL_JUMP` [`00b4f038`](#insn-00b4f038) → [`00b4f068`](#insn-00b4f068)
  - `FALL_THROUGH` [`00b4f038`](#insn-00b4f038) → [`00b4f03c`](#insn-00b4f03c)
- ブロック [`00b4f03c`](#insn-00b4f03c) 範囲 `[['00b4f03c', '00b4f043']]`
  - `CONDITIONAL_JUMP` [`00b4f040`](#insn-00b4f040) → [`00b4f068`](#insn-00b4f068)
  - `FALL_THROUGH` [`00b4f040`](#insn-00b4f040) → [`00b4f044`](#insn-00b4f044)
- ブロック [`00b4f044`](#insn-00b4f044) 範囲 `[['00b4f044', '00b4f04f']]`
  - `FALL_THROUGH` [`00b4f04c`](#insn-00b4f04c) → [`00b4f050`](#insn-00b4f050)
- ブロック [`00b4f050`](#insn-00b4f050) 範囲 `[['00b4f050', '00b4f053']]`
  - `UNCONDITIONAL_JUMP` [`00b4f050`](#insn-00b4f050) → [`00b4f06c`](#insn-00b4f06c)
- ブロック [`00b4f054`](#insn-00b4f054) 範囲 `[['00b4f054', '00b4f057']]`
  - `FALL_THROUGH` [`00b4f054`](#insn-00b4f054) → [`00b4f058`](#insn-00b4f058)
- ブロック [`00b4f058`](#insn-00b4f058) 範囲 `[['00b4f058', '00b4f063']]`
  - `CONDITIONAL_JUMP` [`00b4f060`](#insn-00b4f060) → [`00b4ef64`](#insn-00b4ef64)
  - `FALL_THROUGH` [`00b4f060`](#insn-00b4f060) → [`00b4f064`](#insn-00b4f064)
- ブロック [`00b4f064`](#insn-00b4f064) 範囲 `[['00b4f064', '00b4f067']]`
  - `UNCONDITIONAL_JUMP` [`00b4f064`](#insn-00b4f064) → [`00b4f0c4`](#insn-00b4f0c4)
- ブロック [`00b4f068`](#insn-00b4f068) 範囲 `[['00b4f068', '00b4f06b']]`
  - `FALL_THROUGH` [`00b4f068`](#insn-00b4f068) → [`00b4f06c`](#insn-00b4f06c)
- ブロック [`00b4f06c`](#insn-00b4f06c) 範囲 `[['00b4f06c', '00b4f07f']]`
  - `FALL_THROUGH` [`00b4f07c`](#insn-00b4f07c) → [`00b4f080`](#insn-00b4f080)
- ブロック [`00b4f080`](#insn-00b4f080) 範囲 `[['00b4f080', '00b4f083']]`
  - `CONDITIONAL_JUMP` [`00b4f080`](#insn-00b4f080) → [`00b4ef64`](#insn-00b4ef64)
  - `FALL_THROUGH` [`00b4f080`](#insn-00b4f080) → [`00b4f084`](#insn-00b4f084)
- ブロック [`00b4f084`](#insn-00b4f084) 範囲 `[['00b4f084', '00b4f087']]`
  - `UNCONDITIONAL_JUMP` [`00b4f084`](#insn-00b4f084) → [`00b4f0c4`](#insn-00b4f0c4)
- ブロック [`00b4f088`](#insn-00b4f088) 範囲 `[['00b4f088', '00b4f097']]`
  - `FALL_THROUGH` [`00b4f094`](#insn-00b4f094) → [`00b4f098`](#insn-00b4f098)
- ブロック [`00b4f098`](#insn-00b4f098) 範囲 `[['00b4f098', '00b4f09b']]`
  - `UNCONDITIONAL_JUMP` [`00b4f098`](#insn-00b4f098) → [`00b4f0c0`](#insn-00b4f0c0)
- ブロック [`00b4f09c`](#insn-00b4f09c) 範囲 `[['00b4f09c', '00b4f0af']]`
  - `UNCONDITIONAL_JUMP` [`00b4f0ac`](#insn-00b4f0ac) → [`00b4f0c0`](#insn-00b4f0c0)
- ブロック [`00b4f0b0`](#insn-00b4f0b0) 範囲 `[['00b4f0b0', '00b4f0bb']]`
  - `FALL_THROUGH` [`00b4f0b8`](#insn-00b4f0b8) → [`00b4f0bc`](#insn-00b4f0bc)
- ブロック [`00b4f0bc`](#insn-00b4f0bc) 範囲 `[['00b4f0bc', '00b4f0bf']]`
  - `FALL_THROUGH` [`00b4f0bc`](#insn-00b4f0bc) → [`00b4f0c0`](#insn-00b4f0c0)
- ブロック [`00b4f0c0`](#insn-00b4f0c0) 範囲 `[['00b4f0c0', '00b4f0c3']]`
  - `FALL_THROUGH` [`00b4f0c0`](#insn-00b4f0c0) → [`00b4f0c4`](#insn-00b4f0c4)
- ブロック [`00b4f0c4`](#insn-00b4f0c4) 範囲 `[['00b4f0c4', '00b4f0d3']]`
  - `CONDITIONAL_JUMP` [`00b4f0d0`](#insn-00b4f0d0) → [`00b4f0f4`](#insn-00b4f0f4)
  - `FALL_THROUGH` [`00b4f0d0`](#insn-00b4f0d0) → [`00b4f0d4`](#insn-00b4f0d4)
- ブロック [`00b4f0d4`](#insn-00b4f0d4) 範囲 `[['00b4f0d4', '00b4f0e3']]`
  - `FALL_THROUGH` [`00b4f0e0`](#insn-00b4f0e0) → [`00b4f0e4`](#insn-00b4f0e4)
- ブロック [`00b4f0e4`](#insn-00b4f0e4) 範囲 `[['00b4f0e4', '00b4f0f3']]`
- ブロック [`00b4f0f4`](#insn-00b4f0f4) 範囲 `[['00b4f0f4', '00b4f0f7']]`

## 命令位置別の参照

- [`00b4eed0`](#insn-00b4eed0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4eed4`](#insn-00b4eed4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4eed8`](#insn-00b4eed8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4eedc`](#insn-00b4eedc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4eee0`](#insn-00b4eee0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4eee4`](#insn-00b4eee4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4eef4`](#insn-00b4eef4) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ef0c`](#insn-00b4ef0c) → [`00b4f0c4`](#insn-00b4f0c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ef1c`](#insn-00b4ef1c) → `002b1c10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ef44`](#insn-00b4ef44) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ef4c`](#insn-00b4ef4c) → [`00b4ef6c`](#insn-00b4ef6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ef50`](#insn-00b4ef50) → [`00b4f09c`](#insn-00b4f09c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ef54`](#insn-00b4ef54) → `002f8a58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4ef58`](#insn-00b4ef58) → `002a01bc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4ef5c`](#insn-00b4ef5c) → [`00bdde40`](../00bdd/00bdde40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdde40` · 推定シンボル `None` · 推定型 `None`
- [`00b4ef60`](#insn-00b4ef60) → [`00b4f0c4`](#insn-00b4f0c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ef68`](#insn-00b4ef68) → [`00b4f09c`](#insn-00b4f09c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ef74`](#insn-00b4ef74) → [`00b4f0b0`](#insn-00b4f0b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ef78`](#insn-00b4ef78) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ef80`](#insn-00b4ef80) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ef84`](#insn-00b4ef84) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ef88`](#insn-00b4ef88) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ef8c`](#insn-00b4ef8c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ef90`](#insn-00b4ef90) → [`00b4f088`](#insn-00b4f088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ef9c`](#insn-00b4ef9c) → [`00b4f088`](#insn-00b4f088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4efa8`](#insn-00b4efa8) → [`00b4f088`](#insn-00b4f088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4efb4`](#insn-00b4efb4) → [`00be0500`](../00be0/00be0500.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0500` · 推定シンボル `None` · 推定型 `None`
- [`00b4efb8`](#insn-00b4efb8) → [`00b4f088`](#insn-00b4f088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4efd8`](#insn-00b4efd8) → [`00b4ef54`](#insn-00b4ef54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4efe0`](#insn-00b4efe0) → [`00b4ef54`](#insn-00b4ef54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4efec`](#insn-00b4efec) → [`00b4f018`](#insn-00b4f018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4eff4`](#insn-00b4eff4) → [`00b4ef54`](#insn-00b4ef54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4effc`](#insn-00b4effc) → [`00b4f054`](#insn-00b4f054) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f004`](#insn-00b4f004) → [`00b4f054`](#insn-00b4f054) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f014`](#insn-00b4f014) → [`00b4f058`](#insn-00b4f058) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f038`](#insn-00b4f038) → [`00b4f068`](#insn-00b4f068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f040`](#insn-00b4f040) → [`00b4f068`](#insn-00b4f068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f050`](#insn-00b4f050) → [`00b4f06c`](#insn-00b4f06c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f05c`](#insn-00b4f05c) → [`00be0550`](../00be0/00be0550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0550` · 推定シンボル `None` · 推定型 `None`
- [`00b4f060`](#insn-00b4f060) → [`00b4ef64`](#insn-00b4ef64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f064`](#insn-00b4f064) → [`00b4f0c4`](#insn-00b4f0c4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f078`](#insn-00b4f078) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4f080`](#insn-00b4f080) → [`00b4ef64`](#insn-00b4ef64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f084`](#insn-00b4f084) → [`00b4f0c4`](#insn-00b4f0c4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f090`](#insn-00b4f090) → `002f8a58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4f094`](#insn-00b4f094) → `0029f09f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4f098`](#insn-00b4f098) → [`00b4f0c0`](#insn-00b4f0c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f0a4`](#insn-00b4f0a4) → `002f8a58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4f0a8`](#insn-00b4f0a8) → `00293390`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4f0ac`](#insn-00b4f0ac) → [`00b4f0c0`](#insn-00b4f0c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f0b8`](#insn-00b4f0b8) → `002f8a58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4f0bc`](#insn-00b4f0bc) → `002ab129`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4f0c0`](#insn-00b4f0c0) → [`00bdde40`](../00bdd/00bdde40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdde40` · 推定シンボル `None` · 推定型 `None`
- [`00b4f0c8`](#insn-00b4f0c8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f0d0`](#insn-00b4f0d0) → [`00b4f0f4`](#insn-00b4f0f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f0d4`](#insn-00b4f0d4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f0d8`](#insn-00b4f0d8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f0dc`](#insn-00b4f0dc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f0e0`](#insn-00b4f0e0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f0e4`](#insn-00b4f0e4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f0e8`](#insn-00b4f0e8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4f0f4`](#insn-00b4f0f4) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4eed0`](#insn-00b4eed0)

~~~json
{
  "source": "00b4eed0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4eed4`](#insn-00b4eed4)

~~~json
{
  "source": "00b4eed4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4eed8`](#insn-00b4eed8)

~~~json
{
  "source": "00b4eed8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4eedc`](#insn-00b4eedc)

~~~json
{
  "source": "00b4eedc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4eee0`](#insn-00b4eee0)

~~~json
{
  "source": "00b4eee0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4eee4`](#insn-00b4eee4)

~~~json
{
  "source": "00b4eee4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4eef4`](#insn-00b4eef4)

~~~json
{
  "source": "00b4eef4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ef0c`](#insn-00b4ef0c)

~~~json
{
  "source": "00b4ef0c",
  "target": "00b4f0c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ef1c`](#insn-00b4ef1c)

~~~json
{
  "source": "00b4ef1c",
  "target": "002b1c10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ef44`](#insn-00b4ef44)

~~~json
{
  "source": "00b4ef44",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ef4c`](#insn-00b4ef4c)

~~~json
{
  "source": "00b4ef4c",
  "target": "00b4ef6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ef50`](#insn-00b4ef50)

~~~json
{
  "source": "00b4ef50",
  "target": "00b4f09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ef54`](#insn-00b4ef54)

~~~json
{
  "source": "00b4ef54",
  "target": "002f8a58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002f8a58",
  "offset": 0,
  "size": 242,
  "datatype": "string",
  "bytes": "2573204661696c656420746f206c6f61642046434d206d657373616765732c20",
  "capture_start": "002f8a58",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b4ef58`](#insn-00b4ef58)

~~~json
{
  "source": "00b4ef58",
  "target": "002a01bc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a01bc",
  "offset": 0,
  "size": 33,
  "datatype": "string",
  "bytes": "446574656374656420696e76616c69642046434d206576656e7420747970652e",
  "capture_start": "002a01bc",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b4ef5c`](#insn-00b4ef5c)

~~~json
{
  "source": "00b4ef5c",
  "target": "00bdde40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4ef60`](#insn-00b4ef60)

~~~json
{
  "source": "00b4ef60",
  "target": "00b4f0c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ef68`](#insn-00b4ef68)

~~~json
{
  "source": "00b4ef68",
  "target": "00b4f09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ef74`](#insn-00b4ef74)

~~~json
{
  "source": "00b4ef74",
  "target": "00b4f0b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ef78`](#insn-00b4ef78)

~~~json
{
  "source": "00b4ef78",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ef80`](#insn-00b4ef80)

~~~json
{
  "source": "00b4ef80",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ef84`](#insn-00b4ef84)

~~~json
{
  "source": "00b4ef84",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ef88`](#insn-00b4ef88)

~~~json
{
  "source": "00b4ef88",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ef8c`](#insn-00b4ef8c)

~~~json
{
  "source": "00b4ef8c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ef90`](#insn-00b4ef90)

~~~json
{
  "source": "00b4ef90",
  "target": "00b4f088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ef9c`](#insn-00b4ef9c)

~~~json
{
  "source": "00b4ef9c",
  "target": "00b4f088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4efa8`](#insn-00b4efa8)

~~~json
{
  "source": "00b4efa8",
  "target": "00b4f088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4efb4`](#insn-00b4efb4)

~~~json
{
  "source": "00b4efb4",
  "target": "00be0500",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4efb8`](#insn-00b4efb8)

~~~json
{
  "source": "00b4efb8",
  "target": "00b4f088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4efd8`](#insn-00b4efd8)

~~~json
{
  "source": "00b4efd8",
  "target": "00b4ef54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4efe0`](#insn-00b4efe0)

~~~json
{
  "source": "00b4efe0",
  "target": "00b4ef54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4efec`](#insn-00b4efec)

~~~json
{
  "source": "00b4efec",
  "target": "00b4f018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4eff4`](#insn-00b4eff4)

~~~json
{
  "source": "00b4eff4",
  "target": "00b4ef54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4effc`](#insn-00b4effc)

~~~json
{
  "source": "00b4effc",
  "target": "00b4f054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f004`](#insn-00b4f004)

~~~json
{
  "source": "00b4f004",
  "target": "00b4f054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f014`](#insn-00b4f014)

~~~json
{
  "source": "00b4f014",
  "target": "00b4f058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f038`](#insn-00b4f038)

~~~json
{
  "source": "00b4f038",
  "target": "00b4f068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f040`](#insn-00b4f040)

~~~json
{
  "source": "00b4f040",
  "target": "00b4f068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f050`](#insn-00b4f050)

~~~json
{
  "source": "00b4f050",
  "target": "00b4f06c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f05c`](#insn-00b4f05c)

~~~json
{
  "source": "00b4f05c",
  "target": "00be0550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f060`](#insn-00b4f060)

~~~json
{
  "source": "00b4f060",
  "target": "00b4ef64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f064`](#insn-00b4f064)

~~~json
{
  "source": "00b4f064",
  "target": "00b4f0c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f078`](#insn-00b4f078)

~~~json
{
  "source": "00b4f078",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4f080`](#insn-00b4f080)

~~~json
{
  "source": "00b4f080",
  "target": "00b4ef64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f084`](#insn-00b4f084)

~~~json
{
  "source": "00b4f084",
  "target": "00b4f0c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f090`](#insn-00b4f090)

~~~json
{
  "source": "00b4f090",
  "target": "002f8a58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002f8a58",
  "offset": 0,
  "size": 242,
  "datatype": "string",
  "bytes": "2573204661696c656420746f206c6f61642046434d206d657373616765732c20",
  "capture_start": "002f8a58",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b4f094`](#insn-00b4f094)

~~~json
{
  "source": "00b4f094",
  "target": "0029f09f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029f09f",
  "offset": 0,
  "size": 32,
  "datatype": "string",
  "bytes": "46434d2062756666657220766572696669636174696f6e206661696c65642e00",
  "capture_start": "0029f09f",
  "capture_bytes": 32,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4f098`](#insn-00b4f098)

~~~json
{
  "source": "00b4f098",
  "target": "00b4f0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f0a4`](#insn-00b4f0a4)

~~~json
{
  "source": "00b4f0a4",
  "target": "002f8a58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002f8a58",
  "offset": 0,
  "size": 242,
  "datatype": "string",
  "bytes": "2573204661696c656420746f206c6f61642046434d206d657373616765732c20",
  "capture_start": "002f8a58",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b4f0a8`](#insn-00b4f0a8)

~~~json
{
  "source": "00b4f0a8",
  "target": "00293390",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00293390",
  "offset": 0,
  "size": 48,
  "datatype": "string",
  "bytes": "4465746563746564207072656d617475726520656e64206f6620612046434d20",
  "capture_start": "00293390",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b4f0ac`](#insn-00b4f0ac)

~~~json
{
  "source": "00b4f0ac",
  "target": "00b4f0c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f0b8`](#insn-00b4f0b8)

~~~json
{
  "source": "00b4f0b8",
  "target": "002f8a58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002f8a58",
  "offset": 0,
  "size": 242,
  "datatype": "string",
  "bytes": "2573204661696c656420746f206c6f61642046434d206d657373616765732c20",
  "capture_start": "002f8a58",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b4f0bc`](#insn-00b4f0bc)

~~~json
{
  "source": "00b4f0bc",
  "target": "002ab129",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ab129",
  "offset": 0,
  "size": 37,
  "datatype": "string",
  "bytes": "4465746563746564206d616c666f726d65642046434d206576656e7420686561",
  "capture_start": "002ab129",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b4f0c0`](#insn-00b4f0c0)

~~~json
{
  "source": "00b4f0c0",
  "target": "00bdde40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4f0c8`](#insn-00b4f0c8)

~~~json
{
  "source": "00b4f0c8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f0d0`](#insn-00b4f0d0)

~~~json
{
  "source": "00b4f0d0",
  "target": "00b4f0f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f0d4`](#insn-00b4f0d4)

~~~json
{
  "source": "00b4f0d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f0d8`](#insn-00b4f0d8)

~~~json
{
  "source": "00b4f0d8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f0dc`](#insn-00b4f0dc)

~~~json
{
  "source": "00b4f0dc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f0e0`](#insn-00b4f0e0)

~~~json
{
  "source": "00b4f0e0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f0e4`](#insn-00b4f0e4)

~~~json
{
  "source": "00b4f0e4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f0e8`](#insn-00b4f0e8)

~~~json
{
  "source": "00b4f0e8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4f0f4`](#insn-00b4f0f4)

~~~json
{
  "source": "00b4f0f4",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
