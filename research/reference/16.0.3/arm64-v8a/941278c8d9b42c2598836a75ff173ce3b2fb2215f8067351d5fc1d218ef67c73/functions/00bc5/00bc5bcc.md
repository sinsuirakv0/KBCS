# 00bc5bcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bc4bd8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4bd8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-03219727b5f27b5a9e97f314e6dbde24)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc5bcc",
  "name": "_ZN8firebase13remote_config8internal20RemoteConfigInternal7CleanupEv",
  "size": 956,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "44376e88ab8cba7102192ac1b34440aac27e06e3bc39b9569b179e334a847c30",
  "source_text_sha256": "44376e88ab8cba7102192ac1b34440aac27e06e3bc39b9569b179e334a847c30",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc5bcc",
        "00bc5f87"
      ]
    ],
    "bytes_sha256": "71e81ca595c24080d08ad56a7866096f3b29ce8714785ef0e8923212023393e9",
    "instruction_count": 239,
    "instruction_bytes": 956,
    "body_bytes": 956,
    "indirect": 20,
    "unresolved": 20
  }
}
~~~

## 呼び出し元

- [00c5e8a0](../00c5e/00c5e8a0.md)

## 呼び出し先

- [00c58f80](../00c58/00c58f80.md)
- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bab0](../00c5b/00c5bab0.md)
- [00c5c000](../00c5c/00c5c000.md)
- [00c5c070](../00c5c/00c5c070.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5e9d0](../00c5e/00c5e9d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5681 bytes

~~~c

void _ZN8firebase13remote_config8internal20RemoteConfigInternal7CleanupEv(undefined8 *param_1)

{
  undefined *puVar1;
  int iVar2;
  long lVar3;
  undefined *puVar4;
  long *plVar5;
  undefined *local_48;
  undefined *puStack_40;
  long local_38;
  
  puVar4 = PTR__ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E_00c9ca18;
  lVar3 = tpidr_el0;
  local_38 = *(long *)(lVar3 + 0x28);
  puVar1 = PTR__ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E_00c9ca18 +
           4;
  local_48 = PTR__ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E_00c9ca18;
  puStack_40 = puVar1;
  _ZN8firebase5Mutex7AcquireEv(puVar1);
  _ZN8firebase5Mutex7AcquireEv(puVar1);
  *(int *)puVar4 = *(int *)puVar4 + 1;
  _ZN8firebase5Mutex7ReleaseEv(puVar4 + 4);
  _ZN8firebase5Mutex7AcquireEv(puVar4 + 4);
  iVar2 = *(int *)puVar4;
  if (iVar2 != 0) {
    *(int *)puVar4 = iVar2 + -1;
  }
  _ZN8firebase5Mutex7ReleaseEv(puVar4 + 4);
                    /* try { // try from 00bc5c48 to 00cc5c53 has its CatchHandler @ 00bc6508 */
  if (iVar2 == 2) {
    plVar5 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*param_1);
                    /* try { // try from 00bc5c54 to 00cc5cc7 has its CatchHandler @ 00bc4ce4 */
    if (DAT_01127718 != 0) {
      if (DAT_01127720 != '\0') {
        (**(code **)(*plVar5 + 0x6c0))(plVar5);
        DAT_01127720 = '\0';
      }
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar5);
      (**(code **)(*plVar5 + 0xb0))(plVar5,DAT_01127718);
      DAT_01127718 = 0;
    }
    if (DAT_01127538 != 0) {
      if (DAT_01127540 != '\0') {
                    /* try { // try from 00bc5cc8 to 00cc5cd3 has its CatchHandler @ 00bc6508 */
        (**(code **)(*plVar5 + 0x6c0))(plVar5);
        DAT_01127540 = '\0';
      }
                    /* try { // try from 00bc5cd4 to 00cc5d47 has its CatchHandler @ 00bc4ce4 */
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar5);
      (**(code **)(*plVar5 + 0xb0))(plVar5,DAT_01127538);
      DAT_01127538 = 0;
    }
    if (DAT_011275e0 != 0) {
      if (DAT_011275e8 != '\0') {
        (**(code **)(*plVar5 + 0x6c0))(plVar5);
        DAT_011275e8 = '\0';
      }
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar5);
      (**(code **)(*plVar5 + 0xb0))(plVar5,DAT_011275e0);
      DAT_011275e0 = 0;
    }
    if (DAT_01127628 != 0) {
                    /* try { // try from 00bc5d48 to 00cc5d53 has its CatchHandler @ 00bc6508 */
      if (DAT_01127630 != '\0') {
                    /* try { // try from 00bc5d54 to 00cc5dc7 has its CatchHandler @ 00bc4ce4 */
        (**(code **)(*plVar5 + 0x6c0))(plVar5);
        DAT_01127630 = '\0';
      }
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar5);
      (**(code **)(*plVar5 + 0xb0))(plVar5,DAT_01127628);
      DAT_01127628 = 0;
    }
    if (DAT_01127658 != 0) {
      if (DAT_01127660 != '\0') {
        (**(code **)(*plVar5 + 0x6c0))(plVar5);
        DAT_01127660 = '\0';
      }
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar5);
                    /* try { // try from 00bc5dc8 to 00cc5dd3 has its CatchHandler @ 00bc6508 */
      (**(code **)(*plVar5 + 0xb0))(plVar5,DAT_01127658);
      DAT_01127658 = 0;
    }
                    /* try { // try from 00bc5dd4 to 00cc5e7f has its CatchHandler @ 00bc4ce4 */
    if (DAT_01127680 != 0) {
      if (DAT_01127688 != '\0') {
        (**(code **)(*plVar5 + 0x6c0))(plVar5);
        DAT_01127688 = '\0';
      }
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar5);
      (**(code **)(*plVar5 + 0xb0))(plVar5,DAT_01127680);
      DAT_01127680 = 0;
    }
    if (DAT_011276b8 != 0) {
      if (DAT_011276c0 != '\0') {
        (**(code **)(*plVar5 + 0x6c0))(plVar5);
        DAT_011276c0 = '\0';
      }
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar5);
      (**(code **)(*plVar5 + 0xb0))(plVar5,DAT_011276b8);
      DAT_011276b8 = 0;
    }
    if (DAT_011276f8 != 0) {
                    /* try { // try from 00bc5e80 to 00cc5e8f has its CatchHandler @ 00bc6504 */
      if (DAT_01127700 != '\0') {
                    /* try { // try from 00bc5e90 to 00cc5f03 has its CatchHandler @ 00bc4ce4 */
        (**(code **)(*plVar5 + 0x6c0))(plVar5);
        DAT_01127700 = '\0';
      }
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar5);
      (**(code **)(*plVar5 + 0xb0))(plVar5,DAT_011276f8);
      DAT_011276f8 = 0;
    }
    if (DAT_01127738 != 0) {
      if (DAT_01127740 != '\0') {
        (**(code **)(*plVar5 + 0x6c0))(plVar5);
        DAT_01127740 = '\0';
      }
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar5);
      (**(code **)(*plVar5 + 0xb0))(plVar5,DAT_01127738);
      DAT_01127738 = 0;
    }
                    /* try { // try from 00bc5f04 to 00cc5f0f has its CatchHandler @ 00bc6504 */
    if (DAT_01127758 != 0) {
                    /* try { // try from 00bc5f10 to 00cc5f7b has its CatchHandler @ 00bc4ce4 */
      if (DAT_01127760 != '\0') {
        (**(code **)(*plVar5 + 0x6c0))(plVar5);
        DAT_01127760 = '\0';
      }
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar5);
      (**(code **)(*plVar5 + 0xb0))(plVar5,DAT_01127758);
      DAT_01127758 = 0;
    }
    _ZN8firebase4util9TerminateEP7_JNIEnv(plVar5);
  }
  _ZN8firebase8internal18ReferenceCountLockINS0_14ReferenceCountEED2Ev(&local_48);
  if (*(long *)(lVar3 + 0x28) == local_38) {
                    /* try { // try from 00bc5f7c to 00cc5f87 has its CatchHandler @ 00bc6504 */
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
<a id="insn-00bc5bcc"></a> `00bc5bcc` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bc5bd0"></a> `00bc5bd0` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc5bd4"></a> `00bc5bd4` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bc5bd8"></a> `00bc5bd8` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bc5bdc"></a> `00bc5bdc` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bc5be0"></a> `00bc5be0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bc5be4"></a> `00bc5be4` | `b6 06 00 f0` | adrp x22,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bc5be8"></a> `00bc5be8` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00bc5bec"></a> `00bc5bec` | `d6 0e 45 f9` | ldr x22,[x22, #0xa18] | `FALL_THROUGH`
<a id="insn-00bc5bf0"></a> `00bc5bf0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bc5bf4"></a> `00bc5bf4` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bc5bf8"></a> `00bc5bf8` | `d4 12 00 91` | add x20,x22,#0x4 | `FALL_THROUGH`
<a id="insn-00bc5bfc"></a> `00bc5bfc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bc5c00"></a> `00bc5c00` | `f6 d3 00 a9` | stp x22,x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bc5c04"></a> `00bc5c04` | `a7 57 02 94` | bl 0x00c5baa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc5c08"></a> `00bc5c08` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bc5c0c"></a> `00bc5c0c` | `a5 57 02 94` | bl 0x00c5baa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc5c10"></a> `00bc5c10` | `c8 02 40 b9` | ldr w8,[x22] | `FALL_THROUGH`
<a id="insn-00bc5c14"></a> `00bc5c14` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bc5c18"></a> `00bc5c18` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bc5c1c"></a> `00bc5c1c` | `08 44 00 b8` | str w8,[x0], #0x4 | `FALL_THROUGH`
<a id="insn-00bc5c20"></a> `00bc5c20` | `a4 57 02 94` | bl 0x00c5bab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc5c24"></a> `00bc5c24` | `c0 12 00 91` | add x0,x22,#0x4 | `FALL_THROUGH`
<a id="insn-00bc5c28"></a> `00bc5c28` | `9e 57 02 94` | bl 0x00c5baa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc5c2c"></a> `00bc5c2c` | `d4 02 40 b9` | ldr w20,[x22] | `FALL_THROUGH`
<a id="insn-00bc5c30"></a> `00bc5c30` | `74 00 00 34` | cbz w20,0x00bc5c3c | `CONDITIONAL_JUMP`
<a id="insn-00bc5c34"></a> `00bc5c34` | `88 06 00 51` | sub w8,w20,#0x1 | `FALL_THROUGH`
<a id="insn-00bc5c38"></a> `00bc5c38` | `c8 02 00 b9` | str w8,[x22] | `FALL_THROUGH`
<a id="insn-00bc5c3c"></a> `00bc5c3c` | `c0 12 00 91` | add x0,x22,#0x4 | `FALL_THROUGH`
<a id="insn-00bc5c40"></a> `00bc5c40` | `9c 57 02 94` | bl 0x00c5bab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc5c44"></a> `00bc5c44` | `9f 0a 00 71` | cmp w20,#0x2 | `FALL_THROUGH`
<a id="insn-00bc5c48"></a> `00bc5c48` | `81 18 00 54` | b.ne 0x00bc5f58 | `CONDITIONAL_JUMP`
<a id="insn-00bc5c4c"></a> `00bc5c4c` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bc5c50"></a> `00bc5c50` | `34 59 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bc5c54"></a> `00bc5c54` | `14 2b 00 d0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc5c58"></a> `00bc5c58` | `81 8e 43 f9` | ldr x1,[x20, #0x718] | `FALL_THROUGH`
<a id="insn-00bc5c5c"></a> `00bc5c5c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bc5c60"></a> `00bc5c60` | `21 02 00 b4` | cbz x1,0x00bc5ca4 | `CONDITIONAL_JUMP`
<a id="insn-00bc5c64"></a> `00bc5c64` | `16 2b 00 d0` | adrp x22,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc5c68"></a> `00bc5c68` | `c8 82 5c 39` | ldrb w8,[x22, #0x720] | `FALL_THROUGH`
<a id="insn-00bc5c6c"></a> `00bc5c6c` | `c8 00 00 34` | cbz w8,0x00bc5c84 | `CONDITIONAL_JUMP`
<a id="insn-00bc5c70"></a> `00bc5c70` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc5c74"></a> `00bc5c74` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bc5c78"></a> `00bc5c78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5c7c"></a> `00bc5c7c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc5c80"></a> `00bc5c80` | `df 82 1c 39` | strb wzr,[x22, #0x720] | `FALL_THROUGH`
<a id="insn-00bc5c84"></a> `00bc5c84` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5c88"></a> `00bc5c88` | `de 58 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bc5c8c"></a> `00bc5c8c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc5c90"></a> `00bc5c90` | `81 8e 43 f9` | ldr x1,[x20, #0x718] | `FALL_THROUGH`
<a id="insn-00bc5c94"></a> `00bc5c94` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bc5c98"></a> `00bc5c98` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5c9c"></a> `00bc5c9c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc5ca0"></a> `00bc5ca0` | `9f 8e 03 f9` | str xzr,[x20, #0x718] | `FALL_THROUGH`
<a id="insn-00bc5ca4"></a> `00bc5ca4` | `14 2b 00 d0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc5ca8"></a> `00bc5ca8` | `81 9e 42 f9` | ldr x1,[x20, #0x538] | `FALL_THROUGH`
<a id="insn-00bc5cac"></a> `00bc5cac` | `21 02 00 b4` | cbz x1,0x00bc5cf0 | `CONDITIONAL_JUMP`
<a id="insn-00bc5cb0"></a> `00bc5cb0` | `16 2b 00 d0` | adrp x22,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc5cb4"></a> `00bc5cb4` | `c8 02 55 39` | ldrb w8,[x22, #0x540] | `FALL_THROUGH`
<a id="insn-00bc5cb8"></a> `00bc5cb8` | `c8 00 00 34` | cbz w8,0x00bc5cd0 | `CONDITIONAL_JUMP`
<a id="insn-00bc5cbc"></a> `00bc5cbc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc5cc0"></a> `00bc5cc0` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bc5cc4"></a> `00bc5cc4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5cc8"></a> `00bc5cc8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc5ccc"></a> `00bc5ccc` | `df 02 15 39` | strb wzr,[x22, #0x540] | `FALL_THROUGH`
<a id="insn-00bc5cd0"></a> `00bc5cd0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5cd4"></a> `00bc5cd4` | `cb 58 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bc5cd8"></a> `00bc5cd8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc5cdc"></a> `00bc5cdc` | `81 9e 42 f9` | ldr x1,[x20, #0x538] | `FALL_THROUGH`
<a id="insn-00bc5ce0"></a> `00bc5ce0` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bc5ce4"></a> `00bc5ce4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5ce8"></a> `00bc5ce8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc5cec"></a> `00bc5cec` | `9f 9e 02 f9` | str xzr,[x20, #0x538] | `FALL_THROUGH`
<a id="insn-00bc5cf0"></a> `00bc5cf0` | `14 2b 00 d0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc5cf4"></a> `00bc5cf4` | `81 f2 42 f9` | ldr x1,[x20, #0x5e0] | `FALL_THROUGH`
<a id="insn-00bc5cf8"></a> `00bc5cf8` | `21 02 00 b4` | cbz x1,0x00bc5d3c | `CONDITIONAL_JUMP`
<a id="insn-00bc5cfc"></a> `00bc5cfc` | `16 2b 00 d0` | adrp x22,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc5d00"></a> `00bc5d00` | `c8 a2 57 39` | ldrb w8,[x22, #0x5e8] | `FALL_THROUGH`
<a id="insn-00bc5d04"></a> `00bc5d04` | `c8 00 00 34` | cbz w8,0x00bc5d1c | `CONDITIONAL_JUMP`
<a id="insn-00bc5d08"></a> `00bc5d08` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc5d0c"></a> `00bc5d0c` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bc5d10"></a> `00bc5d10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5d14"></a> `00bc5d14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc5d18"></a> `00bc5d18` | `df a2 17 39` | strb wzr,[x22, #0x5e8] | `FALL_THROUGH`
<a id="insn-00bc5d1c"></a> `00bc5d1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5d20"></a> `00bc5d20` | `b8 58 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bc5d24"></a> `00bc5d24` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc5d28"></a> `00bc5d28` | `81 f2 42 f9` | ldr x1,[x20, #0x5e0] | `FALL_THROUGH`
<a id="insn-00bc5d2c"></a> `00bc5d2c` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bc5d30"></a> `00bc5d30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5d34"></a> `00bc5d34` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc5d38"></a> `00bc5d38` | `9f f2 02 f9` | str xzr,[x20, #0x5e0] | `FALL_THROUGH`
<a id="insn-00bc5d3c"></a> `00bc5d3c` | `14 2b 00 d0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc5d40"></a> `00bc5d40` | `81 16 43 f9` | ldr x1,[x20, #0x628] | `FALL_THROUGH`
<a id="insn-00bc5d44"></a> `00bc5d44` | `21 02 00 b4` | cbz x1,0x00bc5d88 | `CONDITIONAL_JUMP`
<a id="insn-00bc5d48"></a> `00bc5d48` | `16 2b 00 d0` | adrp x22,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc5d4c"></a> `00bc5d4c` | `c8 c2 58 39` | ldrb w8,[x22, #0x630] | `FALL_THROUGH`
<a id="insn-00bc5d50"></a> `00bc5d50` | `c8 00 00 34` | cbz w8,0x00bc5d68 | `CONDITIONAL_JUMP`
<a id="insn-00bc5d54"></a> `00bc5d54` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc5d58"></a> `00bc5d58` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bc5d5c"></a> `00bc5d5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5d60"></a> `00bc5d60` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc5d64"></a> `00bc5d64` | `df c2 18 39` | strb wzr,[x22, #0x630] | `FALL_THROUGH`
<a id="insn-00bc5d68"></a> `00bc5d68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5d6c"></a> `00bc5d6c` | `a5 58 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bc5d70"></a> `00bc5d70` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc5d74"></a> `00bc5d74` | `81 16 43 f9` | ldr x1,[x20, #0x628] | `FALL_THROUGH`
<a id="insn-00bc5d78"></a> `00bc5d78` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bc5d7c"></a> `00bc5d7c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5d80"></a> `00bc5d80` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc5d84"></a> `00bc5d84` | `9f 16 03 f9` | str xzr,[x20, #0x628] | `FALL_THROUGH`
<a id="insn-00bc5d88"></a> `00bc5d88` | `14 2b 00 d0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc5d8c"></a> `00bc5d8c` | `81 2e 43 f9` | ldr x1,[x20, #0x658] | `FALL_THROUGH`
<a id="insn-00bc5d90"></a> `00bc5d90` | `21 02 00 b4` | cbz x1,0x00bc5dd4 | `CONDITIONAL_JUMP`
<a id="insn-00bc5d94"></a> `00bc5d94` | `16 2b 00 d0` | adrp x22,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc5d98"></a> `00bc5d98` | `c8 82 59 39` | ldrb w8,[x22, #0x660] | `FALL_THROUGH`
<a id="insn-00bc5d9c"></a> `00bc5d9c` | `c8 00 00 34` | cbz w8,0x00bc5db4 | `CONDITIONAL_JUMP`
<a id="insn-00bc5da0"></a> `00bc5da0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc5da4"></a> `00bc5da4` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bc5da8"></a> `00bc5da8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5dac"></a> `00bc5dac` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc5db0"></a> `00bc5db0` | `df 82 19 39` | strb wzr,[x22, #0x660] | `FALL_THROUGH`
<a id="insn-00bc5db4"></a> `00bc5db4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5db8"></a> `00bc5db8` | `92 58 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bc5dbc"></a> `00bc5dbc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc5dc0"></a> `00bc5dc0` | `81 2e 43 f9` | ldr x1,[x20, #0x658] | `FALL_THROUGH`
<a id="insn-00bc5dc4"></a> `00bc5dc4` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bc5dc8"></a> `00bc5dc8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5dcc"></a> `00bc5dcc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc5dd0"></a> `00bc5dd0` | `9f 2e 03 f9` | str xzr,[x20, #0x658] | `FALL_THROUGH`
<a id="insn-00bc5dd4"></a> `00bc5dd4` | `14 2b 00 d0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc5dd8"></a> `00bc5dd8` | `81 42 43 f9` | ldr x1,[x20, #0x680] | `FALL_THROUGH`
<a id="insn-00bc5ddc"></a> `00bc5ddc` | `21 02 00 b4` | cbz x1,0x00bc5e20 | `CONDITIONAL_JUMP`
<a id="insn-00bc5de0"></a> `00bc5de0` | `16 2b 00 d0` | adrp x22,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc5de4"></a> `00bc5de4` | `c8 22 5a 39` | ldrb w8,[x22, #0x688] | `FALL_THROUGH`
<a id="insn-00bc5de8"></a> `00bc5de8` | `c8 00 00 34` | cbz w8,0x00bc5e00 | `CONDITIONAL_JUMP`
<a id="insn-00bc5dec"></a> `00bc5dec` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc5df0"></a> `00bc5df0` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bc5df4"></a> `00bc5df4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5df8"></a> `00bc5df8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc5dfc"></a> `00bc5dfc` | `df 22 1a 39` | strb wzr,[x22, #0x688] | `FALL_THROUGH`
<a id="insn-00bc5e00"></a> `00bc5e00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5e04"></a> `00bc5e04` | `7f 58 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bc5e08"></a> `00bc5e08` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc5e0c"></a> `00bc5e0c` | `81 42 43 f9` | ldr x1,[x20, #0x680] | `FALL_THROUGH`
<a id="insn-00bc5e10"></a> `00bc5e10` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bc5e14"></a> `00bc5e14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5e18"></a> `00bc5e18` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc5e1c"></a> `00bc5e1c` | `9f 42 03 f9` | str xzr,[x20, #0x680] | `FALL_THROUGH`
<a id="insn-00bc5e20"></a> `00bc5e20` | `14 2b 00 d0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc5e24"></a> `00bc5e24` | `81 5e 43 f9` | ldr x1,[x20, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bc5e28"></a> `00bc5e28` | `21 02 00 b4` | cbz x1,0x00bc5e6c | `CONDITIONAL_JUMP`
<a id="insn-00bc5e2c"></a> `00bc5e2c` | `16 2b 00 d0` | adrp x22,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc5e30"></a> `00bc5e30` | `c8 02 5b 39` | ldrb w8,[x22, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bc5e34"></a> `00bc5e34` | `c8 00 00 34` | cbz w8,0x00bc5e4c | `CONDITIONAL_JUMP`
<a id="insn-00bc5e38"></a> `00bc5e38` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc5e3c"></a> `00bc5e3c` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bc5e40"></a> `00bc5e40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5e44"></a> `00bc5e44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc5e48"></a> `00bc5e48` | `df 02 1b 39` | strb wzr,[x22, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bc5e4c"></a> `00bc5e4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5e50"></a> `00bc5e50` | `6c 58 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bc5e54"></a> `00bc5e54` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc5e58"></a> `00bc5e58` | `81 5e 43 f9` | ldr x1,[x20, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bc5e5c"></a> `00bc5e5c` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bc5e60"></a> `00bc5e60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5e64"></a> `00bc5e64` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc5e68"></a> `00bc5e68` | `9f 5e 03 f9` | str xzr,[x20, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bc5e6c"></a> `00bc5e6c` | `14 2b 00 d0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc5e70"></a> `00bc5e70` | `81 7e 43 f9` | ldr x1,[x20, #0x6f8] | `FALL_THROUGH`
<a id="insn-00bc5e74"></a> `00bc5e74` | `21 02 00 b4` | cbz x1,0x00bc5eb8 | `CONDITIONAL_JUMP`
<a id="insn-00bc5e78"></a> `00bc5e78` | `16 2b 00 d0` | adrp x22,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc5e7c"></a> `00bc5e7c` | `c8 02 5c 39` | ldrb w8,[x22, #0x700] | `FALL_THROUGH`
<a id="insn-00bc5e80"></a> `00bc5e80` | `c8 00 00 34` | cbz w8,0x00bc5e98 | `CONDITIONAL_JUMP`
<a id="insn-00bc5e84"></a> `00bc5e84` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc5e88"></a> `00bc5e88` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bc5e8c"></a> `00bc5e8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5e90"></a> `00bc5e90` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc5e94"></a> `00bc5e94` | `df 02 1c 39` | strb wzr,[x22, #0x700] | `FALL_THROUGH`
<a id="insn-00bc5e98"></a> `00bc5e98` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5e9c"></a> `00bc5e9c` | `59 58 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bc5ea0"></a> `00bc5ea0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc5ea4"></a> `00bc5ea4` | `81 7e 43 f9` | ldr x1,[x20, #0x6f8] | `FALL_THROUGH`
<a id="insn-00bc5ea8"></a> `00bc5ea8` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bc5eac"></a> `00bc5eac` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5eb0"></a> `00bc5eb0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc5eb4"></a> `00bc5eb4` | `9f 7e 03 f9` | str xzr,[x20, #0x6f8] | `FALL_THROUGH`
<a id="insn-00bc5eb8"></a> `00bc5eb8` | `14 2b 00 d0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc5ebc"></a> `00bc5ebc` | `81 9e 43 f9` | ldr x1,[x20, #0x738] | `FALL_THROUGH`
<a id="insn-00bc5ec0"></a> `00bc5ec0` | `21 02 00 b4` | cbz x1,0x00bc5f04 | `CONDITIONAL_JUMP`
<a id="insn-00bc5ec4"></a> `00bc5ec4` | `16 2b 00 d0` | adrp x22,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc5ec8"></a> `00bc5ec8` | `c8 02 5d 39` | ldrb w8,[x22, #0x740] | `FALL_THROUGH`
<a id="insn-00bc5ecc"></a> `00bc5ecc` | `c8 00 00 34` | cbz w8,0x00bc5ee4 | `CONDITIONAL_JUMP`
<a id="insn-00bc5ed0"></a> `00bc5ed0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc5ed4"></a> `00bc5ed4` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bc5ed8"></a> `00bc5ed8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5edc"></a> `00bc5edc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc5ee0"></a> `00bc5ee0` | `df 02 1d 39` | strb wzr,[x22, #0x740] | `FALL_THROUGH`
<a id="insn-00bc5ee4"></a> `00bc5ee4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5ee8"></a> `00bc5ee8` | `46 58 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bc5eec"></a> `00bc5eec` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc5ef0"></a> `00bc5ef0` | `81 9e 43 f9` | ldr x1,[x20, #0x738] | `FALL_THROUGH`
<a id="insn-00bc5ef4"></a> `00bc5ef4` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bc5ef8"></a> `00bc5ef8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5efc"></a> `00bc5efc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc5f00"></a> `00bc5f00` | `9f 9e 03 f9` | str xzr,[x20, #0x738] | `FALL_THROUGH`
<a id="insn-00bc5f04"></a> `00bc5f04` | `14 2b 00 d0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc5f08"></a> `00bc5f08` | `81 ae 43 f9` | ldr x1,[x20, #0x758] | `FALL_THROUGH`
<a id="insn-00bc5f0c"></a> `00bc5f0c` | `21 02 00 b4` | cbz x1,0x00bc5f50 | `CONDITIONAL_JUMP`
<a id="insn-00bc5f10"></a> `00bc5f10` | `16 2b 00 d0` | adrp x22,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc5f14"></a> `00bc5f14` | `c8 82 5d 39` | ldrb w8,[x22, #0x760] | `FALL_THROUGH`
<a id="insn-00bc5f18"></a> `00bc5f18` | `c8 00 00 34` | cbz w8,0x00bc5f30 | `CONDITIONAL_JUMP`
<a id="insn-00bc5f1c"></a> `00bc5f1c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc5f20"></a> `00bc5f20` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bc5f24"></a> `00bc5f24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5f28"></a> `00bc5f28` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc5f2c"></a> `00bc5f2c` | `df 82 1d 39` | strb wzr,[x22, #0x760] | `FALL_THROUGH`
<a id="insn-00bc5f30"></a> `00bc5f30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5f34"></a> `00bc5f34` | `33 58 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bc5f38"></a> `00bc5f38` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bc5f3c"></a> `00bc5f3c` | `81 ae 43 f9` | ldr x1,[x20, #0x758] | `FALL_THROUGH`
<a id="insn-00bc5f40"></a> `00bc5f40` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bc5f44"></a> `00bc5f44` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5f48"></a> `00bc5f48` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc5f4c"></a> `00bc5f4c` | `9f ae 03 f9` | str xzr,[x20, #0x758] | `FALL_THROUGH`
<a id="insn-00bc5f50"></a> `00bc5f50` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc5f54"></a> `00bc5f54` | `47 58 02 94` | bl 0x00c5c070 | `UNCONDITIONAL_CALL`
<a id="insn-00bc5f58"></a> `00bc5f58` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bc5f5c"></a> `00bc5f5c` | `9d 62 02 94` | bl 0x00c5e9d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc5f60"></a> `00bc5f60` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00bc5f64"></a> `00bc5f64` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bc5f68"></a> `00bc5f68` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bc5f6c"></a> `00bc5f6c` | `c1 00 00 54` | b.ne 0x00bc5f84 | `CONDITIONAL_JUMP`
<a id="insn-00bc5f70"></a> `00bc5f70` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bc5f74"></a> `00bc5f74` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bc5f78"></a> `00bc5f78` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc5f7c"></a> `00bc5f7c` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bc5f80"></a> `00bc5f80` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bc5f84"></a> `00bc5f84` | `ff 4b 02 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc5bcc`](#insn-00bc5bcc) 範囲 `[['00bc5bcc', '00bc5c33']]`
  - `CONDITIONAL_JUMP` [`00bc5c30`](#insn-00bc5c30) → [`00bc5c3c`](#insn-00bc5c3c)
  - `FALL_THROUGH` [`00bc5c30`](#insn-00bc5c30) → [`00bc5c34`](#insn-00bc5c34)
- ブロック [`00bc5c34`](#insn-00bc5c34) 範囲 `[['00bc5c34', '00bc5c3b']]`
  - `FALL_THROUGH` [`00bc5c38`](#insn-00bc5c38) → [`00bc5c3c`](#insn-00bc5c3c)
- ブロック [`00bc5c3c`](#insn-00bc5c3c) 範囲 `[['00bc5c3c', '00bc5c47']]`
  - `FALL_THROUGH` [`00bc5c44`](#insn-00bc5c44) → [`00bc5c48`](#insn-00bc5c48)
- ブロック [`00bc5c48`](#insn-00bc5c48) 範囲 `[['00bc5c48', '00bc5c4b']]`
  - `CONDITIONAL_JUMP` [`00bc5c48`](#insn-00bc5c48) → [`00bc5f58`](#insn-00bc5f58)
  - `FALL_THROUGH` [`00bc5c48`](#insn-00bc5c48) → [`00bc5c4c`](#insn-00bc5c4c)
- ブロック [`00bc5c4c`](#insn-00bc5c4c) 範囲 `[['00bc5c4c', '00bc5c53']]`
  - `FALL_THROUGH` [`00bc5c50`](#insn-00bc5c50) → [`00bc5c54`](#insn-00bc5c54)
- ブロック [`00bc5c54`](#insn-00bc5c54) 範囲 `[['00bc5c54', '00bc5c63']]`
  - `CONDITIONAL_JUMP` [`00bc5c60`](#insn-00bc5c60) → [`00bc5ca4`](#insn-00bc5ca4)
  - `FALL_THROUGH` [`00bc5c60`](#insn-00bc5c60) → [`00bc5c64`](#insn-00bc5c64)
- ブロック [`00bc5c64`](#insn-00bc5c64) 範囲 `[['00bc5c64', '00bc5c6f']]`
  - `CONDITIONAL_JUMP` [`00bc5c6c`](#insn-00bc5c6c) → [`00bc5c84`](#insn-00bc5c84)
  - `FALL_THROUGH` [`00bc5c6c`](#insn-00bc5c6c) → [`00bc5c70`](#insn-00bc5c70)
- ブロック [`00bc5c70`](#insn-00bc5c70) 範囲 `[['00bc5c70', '00bc5c83']]`
  - `FALL_THROUGH` [`00bc5c80`](#insn-00bc5c80) → [`00bc5c84`](#insn-00bc5c84)
- ブロック [`00bc5c84`](#insn-00bc5c84) 範囲 `[['00bc5c84', '00bc5ca3']]`
  - `FALL_THROUGH` [`00bc5ca0`](#insn-00bc5ca0) → [`00bc5ca4`](#insn-00bc5ca4)
- ブロック [`00bc5ca4`](#insn-00bc5ca4) 範囲 `[['00bc5ca4', '00bc5caf']]`
  - `CONDITIONAL_JUMP` [`00bc5cac`](#insn-00bc5cac) → [`00bc5cf0`](#insn-00bc5cf0)
  - `FALL_THROUGH` [`00bc5cac`](#insn-00bc5cac) → [`00bc5cb0`](#insn-00bc5cb0)
- ブロック [`00bc5cb0`](#insn-00bc5cb0) 範囲 `[['00bc5cb0', '00bc5cbb']]`
  - `CONDITIONAL_JUMP` [`00bc5cb8`](#insn-00bc5cb8) → [`00bc5cd0`](#insn-00bc5cd0)
  - `FALL_THROUGH` [`00bc5cb8`](#insn-00bc5cb8) → [`00bc5cbc`](#insn-00bc5cbc)
- ブロック [`00bc5cbc`](#insn-00bc5cbc) 範囲 `[['00bc5cbc', '00bc5cc7']]`
  - `FALL_THROUGH` [`00bc5cc4`](#insn-00bc5cc4) → [`00bc5cc8`](#insn-00bc5cc8)
- ブロック [`00bc5cc8`](#insn-00bc5cc8) 範囲 `[['00bc5cc8', '00bc5ccf']]`
  - `FALL_THROUGH` [`00bc5ccc`](#insn-00bc5ccc) → [`00bc5cd0`](#insn-00bc5cd0)
- ブロック [`00bc5cd0`](#insn-00bc5cd0) 範囲 `[['00bc5cd0', '00bc5cd3']]`
  - `FALL_THROUGH` [`00bc5cd0`](#insn-00bc5cd0) → [`00bc5cd4`](#insn-00bc5cd4)
- ブロック [`00bc5cd4`](#insn-00bc5cd4) 範囲 `[['00bc5cd4', '00bc5cef']]`
  - `FALL_THROUGH` [`00bc5cec`](#insn-00bc5cec) → [`00bc5cf0`](#insn-00bc5cf0)
- ブロック [`00bc5cf0`](#insn-00bc5cf0) 範囲 `[['00bc5cf0', '00bc5cfb']]`
  - `CONDITIONAL_JUMP` [`00bc5cf8`](#insn-00bc5cf8) → [`00bc5d3c`](#insn-00bc5d3c)
  - `FALL_THROUGH` [`00bc5cf8`](#insn-00bc5cf8) → [`00bc5cfc`](#insn-00bc5cfc)
- ブロック [`00bc5cfc`](#insn-00bc5cfc) 範囲 `[['00bc5cfc', '00bc5d07']]`
  - `CONDITIONAL_JUMP` [`00bc5d04`](#insn-00bc5d04) → [`00bc5d1c`](#insn-00bc5d1c)
  - `FALL_THROUGH` [`00bc5d04`](#insn-00bc5d04) → [`00bc5d08`](#insn-00bc5d08)
- ブロック [`00bc5d08`](#insn-00bc5d08) 範囲 `[['00bc5d08', '00bc5d1b']]`
  - `FALL_THROUGH` [`00bc5d18`](#insn-00bc5d18) → [`00bc5d1c`](#insn-00bc5d1c)
- ブロック [`00bc5d1c`](#insn-00bc5d1c) 範囲 `[['00bc5d1c', '00bc5d3b']]`
  - `FALL_THROUGH` [`00bc5d38`](#insn-00bc5d38) → [`00bc5d3c`](#insn-00bc5d3c)
- ブロック [`00bc5d3c`](#insn-00bc5d3c) 範囲 `[['00bc5d3c', '00bc5d47']]`
  - `CONDITIONAL_JUMP` [`00bc5d44`](#insn-00bc5d44) → [`00bc5d88`](#insn-00bc5d88)
  - `FALL_THROUGH` [`00bc5d44`](#insn-00bc5d44) → [`00bc5d48`](#insn-00bc5d48)
- ブロック [`00bc5d48`](#insn-00bc5d48) 範囲 `[['00bc5d48', '00bc5d53']]`
  - `CONDITIONAL_JUMP` [`00bc5d50`](#insn-00bc5d50) → [`00bc5d68`](#insn-00bc5d68)
  - `FALL_THROUGH` [`00bc5d50`](#insn-00bc5d50) → [`00bc5d54`](#insn-00bc5d54)
- ブロック [`00bc5d54`](#insn-00bc5d54) 範囲 `[['00bc5d54', '00bc5d67']]`
  - `FALL_THROUGH` [`00bc5d64`](#insn-00bc5d64) → [`00bc5d68`](#insn-00bc5d68)
- ブロック [`00bc5d68`](#insn-00bc5d68) 範囲 `[['00bc5d68', '00bc5d87']]`
  - `FALL_THROUGH` [`00bc5d84`](#insn-00bc5d84) → [`00bc5d88`](#insn-00bc5d88)
- ブロック [`00bc5d88`](#insn-00bc5d88) 範囲 `[['00bc5d88', '00bc5d93']]`
  - `CONDITIONAL_JUMP` [`00bc5d90`](#insn-00bc5d90) → [`00bc5dd4`](#insn-00bc5dd4)
  - `FALL_THROUGH` [`00bc5d90`](#insn-00bc5d90) → [`00bc5d94`](#insn-00bc5d94)
- ブロック [`00bc5d94`](#insn-00bc5d94) 範囲 `[['00bc5d94', '00bc5d9f']]`
  - `CONDITIONAL_JUMP` [`00bc5d9c`](#insn-00bc5d9c) → [`00bc5db4`](#insn-00bc5db4)
  - `FALL_THROUGH` [`00bc5d9c`](#insn-00bc5d9c) → [`00bc5da0`](#insn-00bc5da0)
- ブロック [`00bc5da0`](#insn-00bc5da0) 範囲 `[['00bc5da0', '00bc5db3']]`
  - `FALL_THROUGH` [`00bc5db0`](#insn-00bc5db0) → [`00bc5db4`](#insn-00bc5db4)
- ブロック [`00bc5db4`](#insn-00bc5db4) 範囲 `[['00bc5db4', '00bc5dc7']]`
  - `FALL_THROUGH` [`00bc5dc4`](#insn-00bc5dc4) → [`00bc5dc8`](#insn-00bc5dc8)
- ブロック [`00bc5dc8`](#insn-00bc5dc8) 範囲 `[['00bc5dc8', '00bc5dd3']]`
  - `FALL_THROUGH` [`00bc5dd0`](#insn-00bc5dd0) → [`00bc5dd4`](#insn-00bc5dd4)
- ブロック [`00bc5dd4`](#insn-00bc5dd4) 範囲 `[['00bc5dd4', '00bc5ddf']]`
  - `CONDITIONAL_JUMP` [`00bc5ddc`](#insn-00bc5ddc) → [`00bc5e20`](#insn-00bc5e20)
  - `FALL_THROUGH` [`00bc5ddc`](#insn-00bc5ddc) → [`00bc5de0`](#insn-00bc5de0)
- ブロック [`00bc5de0`](#insn-00bc5de0) 範囲 `[['00bc5de0', '00bc5deb']]`
  - `CONDITIONAL_JUMP` [`00bc5de8`](#insn-00bc5de8) → [`00bc5e00`](#insn-00bc5e00)
  - `FALL_THROUGH` [`00bc5de8`](#insn-00bc5de8) → [`00bc5dec`](#insn-00bc5dec)
- ブロック [`00bc5dec`](#insn-00bc5dec) 範囲 `[['00bc5dec', '00bc5dff']]`
  - `FALL_THROUGH` [`00bc5dfc`](#insn-00bc5dfc) → [`00bc5e00`](#insn-00bc5e00)
- ブロック [`00bc5e00`](#insn-00bc5e00) 範囲 `[['00bc5e00', '00bc5e1f']]`
  - `FALL_THROUGH` [`00bc5e1c`](#insn-00bc5e1c) → [`00bc5e20`](#insn-00bc5e20)
- ブロック [`00bc5e20`](#insn-00bc5e20) 範囲 `[['00bc5e20', '00bc5e2b']]`
  - `CONDITIONAL_JUMP` [`00bc5e28`](#insn-00bc5e28) → [`00bc5e6c`](#insn-00bc5e6c)
  - `FALL_THROUGH` [`00bc5e28`](#insn-00bc5e28) → [`00bc5e2c`](#insn-00bc5e2c)
- ブロック [`00bc5e2c`](#insn-00bc5e2c) 範囲 `[['00bc5e2c', '00bc5e37']]`
  - `CONDITIONAL_JUMP` [`00bc5e34`](#insn-00bc5e34) → [`00bc5e4c`](#insn-00bc5e4c)
  - `FALL_THROUGH` [`00bc5e34`](#insn-00bc5e34) → [`00bc5e38`](#insn-00bc5e38)
- ブロック [`00bc5e38`](#insn-00bc5e38) 範囲 `[['00bc5e38', '00bc5e4b']]`
  - `FALL_THROUGH` [`00bc5e48`](#insn-00bc5e48) → [`00bc5e4c`](#insn-00bc5e4c)
- ブロック [`00bc5e4c`](#insn-00bc5e4c) 範囲 `[['00bc5e4c', '00bc5e6b']]`
  - `FALL_THROUGH` [`00bc5e68`](#insn-00bc5e68) → [`00bc5e6c`](#insn-00bc5e6c)
- ブロック [`00bc5e6c`](#insn-00bc5e6c) 範囲 `[['00bc5e6c', '00bc5e77']]`
  - `CONDITIONAL_JUMP` [`00bc5e74`](#insn-00bc5e74) → [`00bc5eb8`](#insn-00bc5eb8)
  - `FALL_THROUGH` [`00bc5e74`](#insn-00bc5e74) → [`00bc5e78`](#insn-00bc5e78)
- ブロック [`00bc5e78`](#insn-00bc5e78) 範囲 `[['00bc5e78', '00bc5e7f']]`
  - `FALL_THROUGH` [`00bc5e7c`](#insn-00bc5e7c) → [`00bc5e80`](#insn-00bc5e80)
- ブロック [`00bc5e80`](#insn-00bc5e80) 範囲 `[['00bc5e80', '00bc5e83']]`
  - `CONDITIONAL_JUMP` [`00bc5e80`](#insn-00bc5e80) → [`00bc5e98`](#insn-00bc5e98)
  - `FALL_THROUGH` [`00bc5e80`](#insn-00bc5e80) → [`00bc5e84`](#insn-00bc5e84)
- ブロック [`00bc5e84`](#insn-00bc5e84) 範囲 `[['00bc5e84', '00bc5e8f']]`
  - `FALL_THROUGH` [`00bc5e8c`](#insn-00bc5e8c) → [`00bc5e90`](#insn-00bc5e90)
- ブロック [`00bc5e90`](#insn-00bc5e90) 範囲 `[['00bc5e90', '00bc5e97']]`
  - `FALL_THROUGH` [`00bc5e94`](#insn-00bc5e94) → [`00bc5e98`](#insn-00bc5e98)
- ブロック [`00bc5e98`](#insn-00bc5e98) 範囲 `[['00bc5e98', '00bc5eb7']]`
  - `FALL_THROUGH` [`00bc5eb4`](#insn-00bc5eb4) → [`00bc5eb8`](#insn-00bc5eb8)
- ブロック [`00bc5eb8`](#insn-00bc5eb8) 範囲 `[['00bc5eb8', '00bc5ec3']]`
  - `CONDITIONAL_JUMP` [`00bc5ec0`](#insn-00bc5ec0) → [`00bc5f04`](#insn-00bc5f04)
  - `FALL_THROUGH` [`00bc5ec0`](#insn-00bc5ec0) → [`00bc5ec4`](#insn-00bc5ec4)
- ブロック [`00bc5ec4`](#insn-00bc5ec4) 範囲 `[['00bc5ec4', '00bc5ecf']]`
  - `CONDITIONAL_JUMP` [`00bc5ecc`](#insn-00bc5ecc) → [`00bc5ee4`](#insn-00bc5ee4)
  - `FALL_THROUGH` [`00bc5ecc`](#insn-00bc5ecc) → [`00bc5ed0`](#insn-00bc5ed0)
- ブロック [`00bc5ed0`](#insn-00bc5ed0) 範囲 `[['00bc5ed0', '00bc5ee3']]`
  - `FALL_THROUGH` [`00bc5ee0`](#insn-00bc5ee0) → [`00bc5ee4`](#insn-00bc5ee4)
- ブロック [`00bc5ee4`](#insn-00bc5ee4) 範囲 `[['00bc5ee4', '00bc5f03']]`
  - `FALL_THROUGH` [`00bc5f00`](#insn-00bc5f00) → [`00bc5f04`](#insn-00bc5f04)
- ブロック [`00bc5f04`](#insn-00bc5f04) 範囲 `[['00bc5f04', '00bc5f0f']]`
  - `CONDITIONAL_JUMP` [`00bc5f0c`](#insn-00bc5f0c) → [`00bc5f50`](#insn-00bc5f50)
  - `FALL_THROUGH` [`00bc5f0c`](#insn-00bc5f0c) → [`00bc5f10`](#insn-00bc5f10)
- ブロック [`00bc5f10`](#insn-00bc5f10) 範囲 `[['00bc5f10', '00bc5f1b']]`
  - `CONDITIONAL_JUMP` [`00bc5f18`](#insn-00bc5f18) → [`00bc5f30`](#insn-00bc5f30)
  - `FALL_THROUGH` [`00bc5f18`](#insn-00bc5f18) → [`00bc5f1c`](#insn-00bc5f1c)
- ブロック [`00bc5f1c`](#insn-00bc5f1c) 範囲 `[['00bc5f1c', '00bc5f2f']]`
  - `FALL_THROUGH` [`00bc5f2c`](#insn-00bc5f2c) → [`00bc5f30`](#insn-00bc5f30)
- ブロック [`00bc5f30`](#insn-00bc5f30) 範囲 `[['00bc5f30', '00bc5f4f']]`
  - `FALL_THROUGH` [`00bc5f4c`](#insn-00bc5f4c) → [`00bc5f50`](#insn-00bc5f50)
- ブロック [`00bc5f50`](#insn-00bc5f50) 範囲 `[['00bc5f50', '00bc5f57']]`
  - `FALL_THROUGH` [`00bc5f54`](#insn-00bc5f54) → [`00bc5f58`](#insn-00bc5f58)
- ブロック [`00bc5f58`](#insn-00bc5f58) 範囲 `[['00bc5f58', '00bc5f6f']]`
  - `CONDITIONAL_JUMP` [`00bc5f6c`](#insn-00bc5f6c) → [`00bc5f84`](#insn-00bc5f84)
  - `FALL_THROUGH` [`00bc5f6c`](#insn-00bc5f6c) → [`00bc5f70`](#insn-00bc5f70)
- ブロック [`00bc5f70`](#insn-00bc5f70) 範囲 `[['00bc5f70', '00bc5f7b']]`
  - `FALL_THROUGH` [`00bc5f78`](#insn-00bc5f78) → [`00bc5f7c`](#insn-00bc5f7c)
- ブロック [`00bc5f7c`](#insn-00bc5f7c) 範囲 `[['00bc5f7c', '00bc5f83']]`
- ブロック [`00bc5f84`](#insn-00bc5f84) 範囲 `[['00bc5f84', '00bc5f87']]`

## 命令位置別の参照

- [`00bc5bd0`](#insn-00bc5bd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5bd4`](#insn-00bc5bd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5bd8`](#insn-00bc5bd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5bec`](#insn-00bc5bec) → `00c9ca18`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bc5bf4`](#insn-00bc5bf4) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5bfc`](#insn-00bc5bfc) → `0112777c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5c00`](#insn-00bc5c00) → `01127778`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E` · 推定型 `undefined4`
- [`00bc5c00`](#insn-00bc5c00) → `0112777c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5c00`](#insn-00bc5c00) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5c04`](#insn-00bc5c04) → [`00c5baa0`](../00c5b/00c5baa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5baa0` · 推定シンボル `None` · 推定型 `None`
- [`00bc5c08`](#insn-00bc5c08) → `0112777c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5c0c`](#insn-00bc5c0c) → [`00c5baa0`](../00c5b/00c5baa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5baa0` · 推定シンボル `None` · 推定型 `None`
- [`00bc5c10`](#insn-00bc5c10) → `01127778`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E` · 推定型 `undefined4`
- [`00bc5c1c`](#insn-00bc5c1c) → `01127778`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E` · 推定型 `undefined4`
- [`00bc5c1c`](#insn-00bc5c1c) → `0112777c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5c20`](#insn-00bc5c20) → [`00c5bab0`](../00c5b/00c5bab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bab0` · 推定シンボル `None` · 推定型 `None`
- [`00bc5c24`](#insn-00bc5c24) → `0112777c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5c28`](#insn-00bc5c28) → [`00c5baa0`](../00c5b/00c5baa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5baa0` · 推定シンボル `None` · 推定型 `None`
- [`00bc5c2c`](#insn-00bc5c2c) → `01127778`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E` · 推定型 `undefined4`
- [`00bc5c30`](#insn-00bc5c30) → [`00bc5c3c`](#insn-00bc5c3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5c38`](#insn-00bc5c38) → `01127778`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E` · 推定型 `undefined4`
- [`00bc5c3c`](#insn-00bc5c3c) → `0112777c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5c40`](#insn-00bc5c40) → [`00c5bab0`](../00c5b/00c5bab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bab0` · 推定シンボル `None` · 推定型 `None`
- [`00bc5c48`](#insn-00bc5c48) → [`00bc5f58`](#insn-00bc5f58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5c50`](#insn-00bc5c50) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bc5c58`](#insn-00bc5c58) → `01127718`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5c60`](#insn-00bc5c60) → [`00bc5ca4`](#insn-00bc5ca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5c68`](#insn-00bc5c68) → `01127720`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc5c6c`](#insn-00bc5c6c) → [`00bc5c84`](#insn-00bc5c84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5c80`](#insn-00bc5c80) → `01127720`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc5c88`](#insn-00bc5c88) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bc5c90`](#insn-00bc5c90) → `01127718`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5ca0`](#insn-00bc5ca0) → `01127718`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5ca8`](#insn-00bc5ca8) → `01127538`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5cac`](#insn-00bc5cac) → [`00bc5cf0`](#insn-00bc5cf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5cb4`](#insn-00bc5cb4) → `01127540`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc5cb8`](#insn-00bc5cb8) → [`00bc5cd0`](#insn-00bc5cd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5ccc`](#insn-00bc5ccc) → `01127540`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc5cd4`](#insn-00bc5cd4) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bc5cdc`](#insn-00bc5cdc) → `01127538`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5cec`](#insn-00bc5cec) → `01127538`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5cf4`](#insn-00bc5cf4) → `011275e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5cf8`](#insn-00bc5cf8) → [`00bc5d3c`](#insn-00bc5d3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5d00`](#insn-00bc5d00) → `011275e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc5d04`](#insn-00bc5d04) → [`00bc5d1c`](#insn-00bc5d1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5d18`](#insn-00bc5d18) → `011275e8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc5d20`](#insn-00bc5d20) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bc5d28`](#insn-00bc5d28) → `011275e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5d38`](#insn-00bc5d38) → `011275e0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5d40`](#insn-00bc5d40) → `01127628`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5d44`](#insn-00bc5d44) → [`00bc5d88`](#insn-00bc5d88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5d4c`](#insn-00bc5d4c) → `01127630`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc5d50`](#insn-00bc5d50) → [`00bc5d68`](#insn-00bc5d68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5d64`](#insn-00bc5d64) → `01127630`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc5d6c`](#insn-00bc5d6c) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bc5d74`](#insn-00bc5d74) → `01127628`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5d84`](#insn-00bc5d84) → `01127628`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5d8c`](#insn-00bc5d8c) → `01127658`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5d90`](#insn-00bc5d90) → [`00bc5dd4`](#insn-00bc5dd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5d98`](#insn-00bc5d98) → `01127660`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc5d9c`](#insn-00bc5d9c) → [`00bc5db4`](#insn-00bc5db4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5db0`](#insn-00bc5db0) → `01127660`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc5db8`](#insn-00bc5db8) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bc5dc0`](#insn-00bc5dc0) → `01127658`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5dd0`](#insn-00bc5dd0) → `01127658`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5dd8`](#insn-00bc5dd8) → `01127680`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5ddc`](#insn-00bc5ddc) → [`00bc5e20`](#insn-00bc5e20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5de4`](#insn-00bc5de4) → `01127688`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc5de8`](#insn-00bc5de8) → [`00bc5e00`](#insn-00bc5e00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5dfc`](#insn-00bc5dfc) → `01127688`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc5e04`](#insn-00bc5e04) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bc5e0c`](#insn-00bc5e0c) → `01127680`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5e1c`](#insn-00bc5e1c) → `01127680`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5e24`](#insn-00bc5e24) → `011276b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5e28`](#insn-00bc5e28) → [`00bc5e6c`](#insn-00bc5e6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5e30`](#insn-00bc5e30) → `011276c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc5e34`](#insn-00bc5e34) → [`00bc5e4c`](#insn-00bc5e4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5e48`](#insn-00bc5e48) → `011276c0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc5e50`](#insn-00bc5e50) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bc5e58`](#insn-00bc5e58) → `011276b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5e68`](#insn-00bc5e68) → `011276b8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5e70`](#insn-00bc5e70) → `011276f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5e74`](#insn-00bc5e74) → [`00bc5eb8`](#insn-00bc5eb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5e7c`](#insn-00bc5e7c) → `01127700`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc5e80`](#insn-00bc5e80) → [`00bc5e98`](#insn-00bc5e98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5e94`](#insn-00bc5e94) → `01127700`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc5e9c`](#insn-00bc5e9c) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bc5ea4`](#insn-00bc5ea4) → `011276f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5eb4`](#insn-00bc5eb4) → `011276f8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5ebc`](#insn-00bc5ebc) → `01127738`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5ec0`](#insn-00bc5ec0) → [`00bc5f04`](#insn-00bc5f04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5ec8`](#insn-00bc5ec8) → `01127740`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc5ecc`](#insn-00bc5ecc) → [`00bc5ee4`](#insn-00bc5ee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5ee0`](#insn-00bc5ee0) → `01127740`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc5ee8`](#insn-00bc5ee8) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bc5ef0`](#insn-00bc5ef0) → `01127738`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5f00`](#insn-00bc5f00) → `01127738`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5f08`](#insn-00bc5f08) → `01127758`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5f0c`](#insn-00bc5f0c) → [`00bc5f50`](#insn-00bc5f50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5f14`](#insn-00bc5f14) → `01127760`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc5f18`](#insn-00bc5f18) → [`00bc5f30`](#insn-00bc5f30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5f2c`](#insn-00bc5f2c) → `01127760`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bc5f34`](#insn-00bc5f34) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bc5f3c`](#insn-00bc5f3c) → `01127758`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5f4c`](#insn-00bc5f4c) → `01127758`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc5f54`](#insn-00bc5f54) → [`00c5c070`](../00c5c/00c5c070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c070` · 推定シンボル `None` · 推定型 `None`
- [`00bc5f5c`](#insn-00bc5f5c) → [`00c5e9d0`](../00c5e/00c5e9d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e9d0` · 推定シンボル `None` · 推定型 `None`
- [`00bc5f64`](#insn-00bc5f64) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5f6c`](#insn-00bc5f6c) → [`00bc5f84`](#insn-00bc5f84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5f70`](#insn-00bc5f70) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5f74`](#insn-00bc5f74) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5f78`](#insn-00bc5f78) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5f84`](#insn-00bc5f84) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc5bd0`](#insn-00bc5bd0)

~~~json
{
  "source": "00bc5bd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5bd4`](#insn-00bc5bd4)

~~~json
{
  "source": "00bc5bd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5bd8`](#insn-00bc5bd8)

~~~json
{
  "source": "00bc5bd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5bec`](#insn-00bc5bec)

~~~json
{
  "source": "00bc5bec",
  "target": "00c9ca18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ca18",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bc5bf4`](#insn-00bc5bf4)

~~~json
{
  "source": "00bc5bf4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5bfc`](#insn-00bc5bfc)

~~~json
{
  "source": "00bc5bfc",
  "target": "0112777c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5c00`](#insn-00bc5c00)

~~~json
{
  "source": "00bc5c00",
  "target": "01127778",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127778",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5c00`](#insn-00bc5c00)

~~~json
{
  "source": "00bc5c00",
  "target": "0112777c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5c00`](#insn-00bc5c00)

~~~json
{
  "source": "00bc5c00",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5c04`](#insn-00bc5c04)

~~~json
{
  "source": "00bc5c04",
  "target": "00c5baa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc5c08`](#insn-00bc5c08)

~~~json
{
  "source": "00bc5c08",
  "target": "0112777c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5c0c`](#insn-00bc5c0c)

~~~json
{
  "source": "00bc5c0c",
  "target": "00c5baa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc5c10`](#insn-00bc5c10)

~~~json
{
  "source": "00bc5c10",
  "target": "01127778",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127778",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5c1c`](#insn-00bc5c1c)

~~~json
{
  "source": "00bc5c1c",
  "target": "01127778",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127778",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5c1c`](#insn-00bc5c1c)

~~~json
{
  "source": "00bc5c1c",
  "target": "0112777c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5c20`](#insn-00bc5c20)

~~~json
{
  "source": "00bc5c20",
  "target": "00c5bab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc5c24`](#insn-00bc5c24)

~~~json
{
  "source": "00bc5c24",
  "target": "0112777c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5c28`](#insn-00bc5c28)

~~~json
{
  "source": "00bc5c28",
  "target": "00c5baa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc5c2c`](#insn-00bc5c2c)

~~~json
{
  "source": "00bc5c2c",
  "target": "01127778",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127778",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5c30`](#insn-00bc5c30)

~~~json
{
  "source": "00bc5c30",
  "target": "00bc5c3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5c38`](#insn-00bc5c38)

~~~json
{
  "source": "00bc5c38",
  "target": "01127778",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127778",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5c3c`](#insn-00bc5c3c)

~~~json
{
  "source": "00bc5c3c",
  "target": "0112777c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5c40`](#insn-00bc5c40)

~~~json
{
  "source": "00bc5c40",
  "target": "00c5bab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc5c48`](#insn-00bc5c48)

~~~json
{
  "source": "00bc5c48",
  "target": "00bc5f58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5c50`](#insn-00bc5c50)

~~~json
{
  "source": "00bc5c50",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc5c58`](#insn-00bc5c58)

~~~json
{
  "source": "00bc5c58",
  "target": "01127718",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127718",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5c60`](#insn-00bc5c60)

~~~json
{
  "source": "00bc5c60",
  "target": "00bc5ca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5c68`](#insn-00bc5c68)

~~~json
{
  "source": "00bc5c68",
  "target": "01127720",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127720",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5c6c`](#insn-00bc5c6c)

~~~json
{
  "source": "00bc5c6c",
  "target": "00bc5c84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5c80`](#insn-00bc5c80)

~~~json
{
  "source": "00bc5c80",
  "target": "01127720",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127720",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5c88`](#insn-00bc5c88)

~~~json
{
  "source": "00bc5c88",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc5c90`](#insn-00bc5c90)

~~~json
{
  "source": "00bc5c90",
  "target": "01127718",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127718",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5ca0`](#insn-00bc5ca0)

~~~json
{
  "source": "00bc5ca0",
  "target": "01127718",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127718",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5ca8`](#insn-00bc5ca8)

~~~json
{
  "source": "00bc5ca8",
  "target": "01127538",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127538",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5cac`](#insn-00bc5cac)

~~~json
{
  "source": "00bc5cac",
  "target": "00bc5cf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5cb4`](#insn-00bc5cb4)

~~~json
{
  "source": "00bc5cb4",
  "target": "01127540",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127540",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5cb8`](#insn-00bc5cb8)

~~~json
{
  "source": "00bc5cb8",
  "target": "00bc5cd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5ccc`](#insn-00bc5ccc)

~~~json
{
  "source": "00bc5ccc",
  "target": "01127540",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127540",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5cd4`](#insn-00bc5cd4)

~~~json
{
  "source": "00bc5cd4",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc5cdc`](#insn-00bc5cdc)

~~~json
{
  "source": "00bc5cdc",
  "target": "01127538",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127538",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5cec`](#insn-00bc5cec)

~~~json
{
  "source": "00bc5cec",
  "target": "01127538",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127538",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5cf4`](#insn-00bc5cf4)

~~~json
{
  "source": "00bc5cf4",
  "target": "011275e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011275e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5cf8`](#insn-00bc5cf8)

~~~json
{
  "source": "00bc5cf8",
  "target": "00bc5d3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5d00`](#insn-00bc5d00)

~~~json
{
  "source": "00bc5d00",
  "target": "011275e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011275e8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5d04`](#insn-00bc5d04)

~~~json
{
  "source": "00bc5d04",
  "target": "00bc5d1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5d18`](#insn-00bc5d18)

~~~json
{
  "source": "00bc5d18",
  "target": "011275e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011275e8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5d20`](#insn-00bc5d20)

~~~json
{
  "source": "00bc5d20",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc5d28`](#insn-00bc5d28)

~~~json
{
  "source": "00bc5d28",
  "target": "011275e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011275e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5d38`](#insn-00bc5d38)

~~~json
{
  "source": "00bc5d38",
  "target": "011275e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011275e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5d40`](#insn-00bc5d40)

~~~json
{
  "source": "00bc5d40",
  "target": "01127628",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127628",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5d44`](#insn-00bc5d44)

~~~json
{
  "source": "00bc5d44",
  "target": "00bc5d88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5d4c`](#insn-00bc5d4c)

~~~json
{
  "source": "00bc5d4c",
  "target": "01127630",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127630",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5d50`](#insn-00bc5d50)

~~~json
{
  "source": "00bc5d50",
  "target": "00bc5d68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5d64`](#insn-00bc5d64)

~~~json
{
  "source": "00bc5d64",
  "target": "01127630",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127630",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5d6c`](#insn-00bc5d6c)

~~~json
{
  "source": "00bc5d6c",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc5d74`](#insn-00bc5d74)

~~~json
{
  "source": "00bc5d74",
  "target": "01127628",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127628",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5d84`](#insn-00bc5d84)

~~~json
{
  "source": "00bc5d84",
  "target": "01127628",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127628",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5d8c`](#insn-00bc5d8c)

~~~json
{
  "source": "00bc5d8c",
  "target": "01127658",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127658",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5d90`](#insn-00bc5d90)

~~~json
{
  "source": "00bc5d90",
  "target": "00bc5dd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5d98`](#insn-00bc5d98)

~~~json
{
  "source": "00bc5d98",
  "target": "01127660",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127660",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5d9c`](#insn-00bc5d9c)

~~~json
{
  "source": "00bc5d9c",
  "target": "00bc5db4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5db0`](#insn-00bc5db0)

~~~json
{
  "source": "00bc5db0",
  "target": "01127660",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127660",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5db8`](#insn-00bc5db8)

~~~json
{
  "source": "00bc5db8",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc5dc0`](#insn-00bc5dc0)

~~~json
{
  "source": "00bc5dc0",
  "target": "01127658",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127658",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5dd0`](#insn-00bc5dd0)

~~~json
{
  "source": "00bc5dd0",
  "target": "01127658",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127658",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5dd8`](#insn-00bc5dd8)

~~~json
{
  "source": "00bc5dd8",
  "target": "01127680",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127680",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5ddc`](#insn-00bc5ddc)

~~~json
{
  "source": "00bc5ddc",
  "target": "00bc5e20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5de4`](#insn-00bc5de4)

~~~json
{
  "source": "00bc5de4",
  "target": "01127688",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127688",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5de8`](#insn-00bc5de8)

~~~json
{
  "source": "00bc5de8",
  "target": "00bc5e00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5dfc`](#insn-00bc5dfc)

~~~json
{
  "source": "00bc5dfc",
  "target": "01127688",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127688",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5e04`](#insn-00bc5e04)

~~~json
{
  "source": "00bc5e04",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc5e0c`](#insn-00bc5e0c)

~~~json
{
  "source": "00bc5e0c",
  "target": "01127680",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127680",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5e1c`](#insn-00bc5e1c)

~~~json
{
  "source": "00bc5e1c",
  "target": "01127680",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127680",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5e24`](#insn-00bc5e24)

~~~json
{
  "source": "00bc5e24",
  "target": "011276b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011276b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5e28`](#insn-00bc5e28)

~~~json
{
  "source": "00bc5e28",
  "target": "00bc5e6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5e30`](#insn-00bc5e30)

~~~json
{
  "source": "00bc5e30",
  "target": "011276c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011276c0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5e34`](#insn-00bc5e34)

~~~json
{
  "source": "00bc5e34",
  "target": "00bc5e4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5e48`](#insn-00bc5e48)

~~~json
{
  "source": "00bc5e48",
  "target": "011276c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011276c0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5e50`](#insn-00bc5e50)

~~~json
{
  "source": "00bc5e50",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc5e58`](#insn-00bc5e58)

~~~json
{
  "source": "00bc5e58",
  "target": "011276b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011276b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5e68`](#insn-00bc5e68)

~~~json
{
  "source": "00bc5e68",
  "target": "011276b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011276b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5e70`](#insn-00bc5e70)

~~~json
{
  "source": "00bc5e70",
  "target": "011276f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011276f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5e74`](#insn-00bc5e74)

~~~json
{
  "source": "00bc5e74",
  "target": "00bc5eb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5e7c`](#insn-00bc5e7c)

~~~json
{
  "source": "00bc5e7c",
  "target": "01127700",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127700",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5e80`](#insn-00bc5e80)

~~~json
{
  "source": "00bc5e80",
  "target": "00bc5e98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5e94`](#insn-00bc5e94)

~~~json
{
  "source": "00bc5e94",
  "target": "01127700",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127700",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5e9c`](#insn-00bc5e9c)

~~~json
{
  "source": "00bc5e9c",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc5ea4`](#insn-00bc5ea4)

~~~json
{
  "source": "00bc5ea4",
  "target": "011276f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011276f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5eb4`](#insn-00bc5eb4)

~~~json
{
  "source": "00bc5eb4",
  "target": "011276f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011276f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5ebc`](#insn-00bc5ebc)

~~~json
{
  "source": "00bc5ebc",
  "target": "01127738",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127738",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5ec0`](#insn-00bc5ec0)

~~~json
{
  "source": "00bc5ec0",
  "target": "00bc5f04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5ec8`](#insn-00bc5ec8)

~~~json
{
  "source": "00bc5ec8",
  "target": "01127740",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127740",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5ecc`](#insn-00bc5ecc)

~~~json
{
  "source": "00bc5ecc",
  "target": "00bc5ee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5ee0`](#insn-00bc5ee0)

~~~json
{
  "source": "00bc5ee0",
  "target": "01127740",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127740",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5ee8`](#insn-00bc5ee8)

~~~json
{
  "source": "00bc5ee8",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc5ef0`](#insn-00bc5ef0)

~~~json
{
  "source": "00bc5ef0",
  "target": "01127738",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127738",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5f00`](#insn-00bc5f00)

~~~json
{
  "source": "00bc5f00",
  "target": "01127738",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127738",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5f08`](#insn-00bc5f08)

~~~json
{
  "source": "00bc5f08",
  "target": "01127758",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127758",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5f0c`](#insn-00bc5f0c)

~~~json
{
  "source": "00bc5f0c",
  "target": "00bc5f50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5f14`](#insn-00bc5f14)

~~~json
{
  "source": "00bc5f14",
  "target": "01127760",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127760",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5f18`](#insn-00bc5f18)

~~~json
{
  "source": "00bc5f18",
  "target": "00bc5f30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5f2c`](#insn-00bc5f2c)

~~~json
{
  "source": "00bc5f2c",
  "target": "01127760",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127760",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5f34`](#insn-00bc5f34)

~~~json
{
  "source": "00bc5f34",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc5f3c`](#insn-00bc5f3c)

~~~json
{
  "source": "00bc5f3c",
  "target": "01127758",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127758",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5f4c`](#insn-00bc5f4c)

~~~json
{
  "source": "00bc5f4c",
  "target": "01127758",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127758",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc5f54`](#insn-00bc5f54)

~~~json
{
  "source": "00bc5f54",
  "target": "00c5c070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc5f5c`](#insn-00bc5f5c)

~~~json
{
  "source": "00bc5f5c",
  "target": "00c5e9d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc5f64`](#insn-00bc5f64)

~~~json
{
  "source": "00bc5f64",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5f6c`](#insn-00bc5f6c)

~~~json
{
  "source": "00bc5f6c",
  "target": "00bc5f84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5f70`](#insn-00bc5f70)

~~~json
{
  "source": "00bc5f70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5f74`](#insn-00bc5f74)

~~~json
{
  "source": "00bc5f74",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5f78`](#insn-00bc5f78)

~~~json
{
  "source": "00bc5f78",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5f84`](#insn-00bc5f84)

~~~json
{
  "source": "00bc5f84",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
