# 00afbe6c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afbf34`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbf34.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-52d220b784e85591ed909fac4e4f7566)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afbe6c",
  "name": "_ZN8firebase8callback18CallbackDispatcher17DispatchCallbacksEv",
  "size": 312,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3d206ec3bdaedb96924588e5ab21d61f73577f4552f14b94e02494f013991868",
  "source_text_sha256": "3d206ec3bdaedb96924588e5ab21d61f73577f4552f14b94e02494f013991868",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afbe6c",
        "00afbfa3"
      ]
    ],
    "bytes_sha256": "dbaee4cdd0eeecb8b2eca1e4253d0ff8d5fb5427d24f998dabeef77e88b24e91",
    "instruction_count": 78,
    "instruction_bytes": 312,
    "body_bytes": 312,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00bdeb70](../00bde/00bdeb70.md)

## 呼び出し先

- [00bdaf30](../00bda/00bdaf30.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)
- [00bdeb40](../00bde/00bdeb40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3232 bytes

~~~c

int _ZN8firebase8callback18CallbackDispatcher17DispatchCallbacksEv(long param_1)

{
  long lVar1;
  long *plVar2;
  long lVar3;
  long lVar4;
  long *plVar5;
  char cVar6;
  bool bVar7;
  long lVar8;
  int iVar9;
  long *plVar10;
  long *plVar11;
  
  lVar1 = param_1 + 0x18;
                    /* try { // try from 00afbe88 to 00bfbe93 has its CatchHandler @ 00b0044c */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  lVar8 = *(long *)(param_1 + 0x10);
                    /* try { // try from 00afbe98 to 00bfbea3 has its CatchHandler @ 00b00444 */
  if (lVar8 == 0) {
    iVar9 = 0;
  }
  else {
    iVar9 = 0;
    do {
      plVar10 = *(long **)(param_1 + 8);
      lVar3 = plVar10[2];
      plVar5 = (long *)plVar10[3];
                    /* try { // try from 00afbeb4 to 00bfbec7 has its CatchHandler @ 00b00448 */
      if (plVar5 != (long *)0x0) {
        plVar10 = plVar5 + 1;
        do {
          cVar6 = '\x01';
          bVar7 = (bool)ExclusiveMonitorPass(plVar10,0x10);
          if (bVar7) {
            *plVar10 = *plVar10 + 1;
            cVar6 = ExclusiveMonitorsStatus();
          }
        } while (cVar6 != '\0');
        plVar10 = *(long **)(param_1 + 8);
        lVar8 = *(long *)(param_1 + 0x10);
      }
      lVar4 = *plVar10;
      *(long *)(lVar4 + 8) = plVar10[1];
      *(long *)plVar10[1] = lVar4;
      *(long *)(param_1 + 0x10) = lVar8 + -1;
      plVar11 = (long *)plVar10[3];
      if (plVar11 != (long *)0x0) {
        plVar2 = plVar11 + 1;
        do {
          lVar8 = *plVar2;
          cVar6 = '\x01';
          bVar7 = (bool)ExclusiveMonitorPass(plVar2,0x10);
          if (bVar7) {
            *plVar2 = lVar8 + -1;
            cVar6 = ExclusiveMonitorsStatus();
          }
        } while (cVar6 != '\0');
        if (lVar8 == 0) {
          (**(code **)(*plVar11 + 0x10))(plVar11);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar11);
        }
      }
      _ZdlPv(plVar10);
      _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* try { // try from 00afbf34 to 00bfbf47 has its CatchHandler @ 00b0040c */
      _ZN8firebase8callback13CallbackEntry7ExecuteEv(lVar3);
      iVar9 = iVar9 + 1;
      _ZN8firebase5Mutex7AcquireEv(lVar1);
      if (plVar5 != (long *)0x0) {
                    /* try { // try from 00afbf48 to 00bfbf4f has its CatchHandler @ 00b003f4 */
        plVar10 = plVar5 + 1;
        do {
          lVar8 = *plVar10;
          cVar6 = '\x01';
          bVar7 = (bool)ExclusiveMonitorPass(plVar10,0x10);
          if (bVar7) {
            *plVar10 = lVar8 + -1;
            cVar6 = ExclusiveMonitorsStatus();
          }
        } while (cVar6 != '\0');
        if (lVar8 == 0) {
          (**(code **)(*plVar5 + 0x10))(plVar5);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar5);
                    /* try { // try from 00afbf78 to 00bfbf8b has its CatchHandler @ 00b003d0 */
        }
      }
                    /* try { // try from 00afbea4 to 00bfbeb3 has its CatchHandler @ 00b00440 */
      lVar8 = *(long *)(param_1 + 0x10);
    } while (lVar8 != 0);
  }
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* try { // try from 00afbf8c to 00bfbfa7 has its CatchHandler @ 00b003b0 */
  return iVar9;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afbe6c"></a> `00afbe6c` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00afbe70"></a> `00afbe70` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbe74"></a> `00afbe74` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afbe78"></a> `00afbe78` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afbe7c"></a> `00afbe7c` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afbe80"></a> `00afbe80` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00afbe84"></a> `00afbe84` | `13 60 00 91` | add x19,x0,#0x18 | `FALL_THROUGH`
<a id="insn-00afbe88"></a> `00afbe88` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00afbe8c"></a> `00afbe8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afbe90"></a> `00afbe90` | `24 87 03 94` | bl 0x00bddb20 | `UNCONDITIONAL_CALL`
<a id="insn-00afbe94"></a> `00afbe94` | `88 0a 40 f9` | ldr x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00afbe98"></a> `00afbe98` | `28 07 00 b4` | cbz x8,0x00afbf7c | `CONDITIONAL_JUMP`
<a id="insn-00afbe9c"></a> `00afbe9c` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-00afbea0"></a> `00afbea0` | `03 00 00 14` | b 0x00afbeac | `UNCONDITIONAL_JUMP`
<a id="insn-00afbea4"></a> `00afbea4` | `88 0a 40 f9` | ldr x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00afbea8"></a> `00afbea8` | `c8 06 00 b4` | cbz x8,0x00afbf80 | `CONDITIONAL_JUMP`
<a id="insn-00afbeac"></a> `00afbeac` | `98 06 40 f9` | ldr x24,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00afbeb0"></a> `00afbeb0` | `17 5b 41 a9` | ldp x23,x22,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00afbeb4"></a> `00afbeb4` | `f6 00 00 b4` | cbz x22,0x00afbed0 | `CONDITIONAL_JUMP`
<a id="insn-00afbeb8"></a> `00afbeb8` | `c8 22 00 91` | add x8,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00afbebc"></a> `00afbebc` | `09 7d 5f c8` | ldxr x9,[x8] | `FALL_THROUGH`
<a id="insn-00afbec0"></a> `00afbec0` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afbec4"></a> `00afbec4` | `09 7d 0a c8` | stxr w10,x9,[x8] | `FALL_THROUGH`
<a id="insn-00afbec8"></a> `00afbec8` | `aa ff ff 35` | cbnz w10,0x00afbebc | `CONDITIONAL_JUMP`
<a id="insn-00afbecc"></a> `00afbecc` | `98 a2 40 a9` | ldp x24,x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00afbed0"></a> `00afbed0` | `09 2b 40 a9` | ldp x9,x10,[x24] | `FALL_THROUGH`
<a id="insn-00afbed4"></a> `00afbed4` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afbed8"></a> `00afbed8` | `2a 05 00 f9` | str x10,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00afbedc"></a> `00afbedc` | `0a 07 40 f9` | ldr x10,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00afbee0"></a> `00afbee0` | `49 01 00 f9` | str x9,[x10] | `FALL_THROUGH`
<a id="insn-00afbee4"></a> `00afbee4` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00afbee8"></a> `00afbee8` | `19 0f 40 f9` | ldr x25,[x24, #0x18] | `FALL_THROUGH`
<a id="insn-00afbeec"></a> `00afbeec` | `b9 01 00 b4` | cbz x25,0x00afbf20 | `CONDITIONAL_JUMP`
<a id="insn-00afbef0"></a> `00afbef0` | `28 23 00 91` | add x8,x25,#0x8 | `FALL_THROUGH`
<a id="insn-00afbef4"></a> `00afbef4` | `09 fd 5f c8` | ldaxr x9,[x8] | `FALL_THROUGH`
<a id="insn-00afbef8"></a> `00afbef8` | `2a 05 00 d1` | sub x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afbefc"></a> `00afbefc` | `0a fd 0b c8` | stlxr w11,x10,[x8] | `FALL_THROUGH`
<a id="insn-00afbf00"></a> `00afbf00` | `ab ff ff 35` | cbnz w11,0x00afbef4 | `CONDITIONAL_JUMP`
<a id="insn-00afbf04"></a> `00afbf04` | `e9 00 00 b5` | cbnz x9,0x00afbf20 | `CONDITIONAL_JUMP`
<a id="insn-00afbf08"></a> `00afbf08` | `28 03 40 f9` | ldr x8,[x25] | `FALL_THROUGH`
<a id="insn-00afbf0c"></a> `00afbf0c` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00afbf10"></a> `00afbf10` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00afbf14"></a> `00afbf14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afbf18"></a> `00afbf18` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00afbf1c"></a> `00afbf1c` | `05 7c 03 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00afbf20"></a> `00afbf20` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00afbf24"></a> `00afbf24` | `0f 7c 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00afbf28"></a> `00afbf28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afbf2c"></a> `00afbf2c` | `01 87 03 94` | bl 0x00bddb30 | `UNCONDITIONAL_CALL`
<a id="insn-00afbf30"></a> `00afbf30` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00afbf34"></a> `00afbf34` | `03 8b 03 94` | bl 0x00bdeb40 | `UNCONDITIONAL_CALL`
<a id="insn-00afbf38"></a> `00afbf38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afbf3c"></a> `00afbf3c` | `b5 06 00 11` | add w21,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00afbf40"></a> `00afbf40` | `f8 86 03 94` | bl 0x00bddb20 | `UNCONDITIONAL_CALL`
<a id="insn-00afbf44"></a> `00afbf44` | `16 fb ff b4` | cbz x22,0x00afbea4 | `CONDITIONAL_JUMP`
<a id="insn-00afbf48"></a> `00afbf48` | `c8 22 00 91` | add x8,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00afbf4c"></a> `00afbf4c` | `09 fd 5f c8` | ldaxr x9,[x8] | `FALL_THROUGH`
<a id="insn-00afbf50"></a> `00afbf50` | `2a 05 00 d1` | sub x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afbf54"></a> `00afbf54` | `0a fd 0b c8` | stlxr w11,x10,[x8] | `FALL_THROUGH`
<a id="insn-00afbf58"></a> `00afbf58` | `ab ff ff 35` | cbnz w11,0x00afbf4c | `CONDITIONAL_JUMP`
<a id="insn-00afbf5c"></a> `00afbf5c` | `49 fa ff b5` | cbnz x9,0x00afbea4 | `CONDITIONAL_JUMP`
<a id="insn-00afbf60"></a> `00afbf60` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00afbf64"></a> `00afbf64` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00afbf68"></a> `00afbf68` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00afbf6c"></a> `00afbf6c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afbf70"></a> `00afbf70` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00afbf74"></a> `00afbf74` | `ef 7b 03 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00afbf78"></a> `00afbf78` | `cb ff ff 17` | b 0x00afbea4 | `UNCONDITIONAL_JUMP`
<a id="insn-00afbf7c"></a> `00afbf7c` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-00afbf80"></a> `00afbf80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afbf84"></a> `00afbf84` | `eb 86 03 94` | bl 0x00bddb30 | `UNCONDITIONAL_CALL`
<a id="insn-00afbf88"></a> `00afbf88` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00afbf8c"></a> `00afbf8c` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afbf90"></a> `00afbf90` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afbf94"></a> `00afbf94` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afbf98"></a> `00afbf98` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbf9c"></a> `00afbf9c` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00afbfa0"></a> `00afbfa0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afbe6c`](#insn-00afbe6c) 範囲 `[['00afbe6c', '00afbe87']]`
  - `FALL_THROUGH` [`00afbe84`](#insn-00afbe84) → [`00afbe88`](#insn-00afbe88)
- ブロック [`00afbe88`](#insn-00afbe88) 範囲 `[['00afbe88', '00afbe97']]`
  - `FALL_THROUGH` [`00afbe94`](#insn-00afbe94) → [`00afbe98`](#insn-00afbe98)
- ブロック [`00afbe98`](#insn-00afbe98) 範囲 `[['00afbe98', '00afbe9b']]`
  - `CONDITIONAL_JUMP` [`00afbe98`](#insn-00afbe98) → [`00afbf7c`](#insn-00afbf7c)
  - `FALL_THROUGH` [`00afbe98`](#insn-00afbe98) → [`00afbe9c`](#insn-00afbe9c)
- ブロック [`00afbe9c`](#insn-00afbe9c) 範囲 `[['00afbe9c', '00afbea3']]`
  - `UNCONDITIONAL_JUMP` [`00afbea0`](#insn-00afbea0) → [`00afbeac`](#insn-00afbeac)
- ブロック [`00afbea4`](#insn-00afbea4) 範囲 `[['00afbea4', '00afbeab']]`
  - `CONDITIONAL_JUMP` [`00afbea8`](#insn-00afbea8) → [`00afbf80`](#insn-00afbf80)
  - `FALL_THROUGH` [`00afbea8`](#insn-00afbea8) → [`00afbeac`](#insn-00afbeac)
- ブロック [`00afbeac`](#insn-00afbeac) 範囲 `[['00afbeac', '00afbeb3']]`
  - `FALL_THROUGH` [`00afbeb0`](#insn-00afbeb0) → [`00afbeb4`](#insn-00afbeb4)
- ブロック [`00afbeb4`](#insn-00afbeb4) 範囲 `[['00afbeb4', '00afbeb7']]`
  - `CONDITIONAL_JUMP` [`00afbeb4`](#insn-00afbeb4) → [`00afbed0`](#insn-00afbed0)
  - `FALL_THROUGH` [`00afbeb4`](#insn-00afbeb4) → [`00afbeb8`](#insn-00afbeb8)
- ブロック [`00afbeb8`](#insn-00afbeb8) 範囲 `[['00afbeb8', '00afbebb']]`
  - `FALL_THROUGH` [`00afbeb8`](#insn-00afbeb8) → [`00afbebc`](#insn-00afbebc)
- ブロック [`00afbebc`](#insn-00afbebc) 範囲 `[['00afbebc', '00afbecb']]`
  - `CONDITIONAL_JUMP` [`00afbec8`](#insn-00afbec8) → [`00afbebc`](#insn-00afbebc)
  - `FALL_THROUGH` [`00afbec8`](#insn-00afbec8) → [`00afbecc`](#insn-00afbecc)
- ブロック [`00afbecc`](#insn-00afbecc) 範囲 `[['00afbecc', '00afbecf']]`
  - `FALL_THROUGH` [`00afbecc`](#insn-00afbecc) → [`00afbed0`](#insn-00afbed0)
- ブロック [`00afbed0`](#insn-00afbed0) 範囲 `[['00afbed0', '00afbeef']]`
  - `CONDITIONAL_JUMP` [`00afbeec`](#insn-00afbeec) → [`00afbf20`](#insn-00afbf20)
  - `FALL_THROUGH` [`00afbeec`](#insn-00afbeec) → [`00afbef0`](#insn-00afbef0)
- ブロック [`00afbef0`](#insn-00afbef0) 範囲 `[['00afbef0', '00afbef3']]`
  - `FALL_THROUGH` [`00afbef0`](#insn-00afbef0) → [`00afbef4`](#insn-00afbef4)
- ブロック [`00afbef4`](#insn-00afbef4) 範囲 `[['00afbef4', '00afbf03']]`
  - `CONDITIONAL_JUMP` [`00afbf00`](#insn-00afbf00) → [`00afbef4`](#insn-00afbef4)
  - `FALL_THROUGH` [`00afbf00`](#insn-00afbf00) → [`00afbf04`](#insn-00afbf04)
- ブロック [`00afbf04`](#insn-00afbf04) 範囲 `[['00afbf04', '00afbf07']]`
  - `CONDITIONAL_JUMP` [`00afbf04`](#insn-00afbf04) → [`00afbf20`](#insn-00afbf20)
  - `FALL_THROUGH` [`00afbf04`](#insn-00afbf04) → [`00afbf08`](#insn-00afbf08)
- ブロック [`00afbf08`](#insn-00afbf08) 範囲 `[['00afbf08', '00afbf1f']]`
  - `FALL_THROUGH` [`00afbf1c`](#insn-00afbf1c) → [`00afbf20`](#insn-00afbf20)
- ブロック [`00afbf20`](#insn-00afbf20) 範囲 `[['00afbf20', '00afbf33']]`
  - `FALL_THROUGH` [`00afbf30`](#insn-00afbf30) → [`00afbf34`](#insn-00afbf34)
- ブロック [`00afbf34`](#insn-00afbf34) 範囲 `[['00afbf34', '00afbf47']]`
  - `CONDITIONAL_JUMP` [`00afbf44`](#insn-00afbf44) → [`00afbea4`](#insn-00afbea4)
  - `FALL_THROUGH` [`00afbf44`](#insn-00afbf44) → [`00afbf48`](#insn-00afbf48)
- ブロック [`00afbf48`](#insn-00afbf48) 範囲 `[['00afbf48', '00afbf4b']]`
  - `FALL_THROUGH` [`00afbf48`](#insn-00afbf48) → [`00afbf4c`](#insn-00afbf4c)
- ブロック [`00afbf4c`](#insn-00afbf4c) 範囲 `[['00afbf4c', '00afbf5b']]`
  - `CONDITIONAL_JUMP` [`00afbf58`](#insn-00afbf58) → [`00afbf4c`](#insn-00afbf4c)
  - `FALL_THROUGH` [`00afbf58`](#insn-00afbf58) → [`00afbf5c`](#insn-00afbf5c)
- ブロック [`00afbf5c`](#insn-00afbf5c) 範囲 `[['00afbf5c', '00afbf5f']]`
  - `CONDITIONAL_JUMP` [`00afbf5c`](#insn-00afbf5c) → [`00afbea4`](#insn-00afbea4)
  - `FALL_THROUGH` [`00afbf5c`](#insn-00afbf5c) → [`00afbf60`](#insn-00afbf60)
- ブロック [`00afbf60`](#insn-00afbf60) 範囲 `[['00afbf60', '00afbf77']]`
  - `FALL_THROUGH` [`00afbf74`](#insn-00afbf74) → [`00afbf78`](#insn-00afbf78)
- ブロック [`00afbf78`](#insn-00afbf78) 範囲 `[['00afbf78', '00afbf7b']]`
  - `UNCONDITIONAL_JUMP` [`00afbf78`](#insn-00afbf78) → [`00afbea4`](#insn-00afbea4)
- ブロック [`00afbf7c`](#insn-00afbf7c) 範囲 `[['00afbf7c', '00afbf7f']]`
  - `FALL_THROUGH` [`00afbf7c`](#insn-00afbf7c) → [`00afbf80`](#insn-00afbf80)
- ブロック [`00afbf80`](#insn-00afbf80) 範囲 `[['00afbf80', '00afbf8b']]`
  - `FALL_THROUGH` [`00afbf88`](#insn-00afbf88) → [`00afbf8c`](#insn-00afbf8c)
- ブロック [`00afbf8c`](#insn-00afbf8c) 範囲 `[['00afbf8c', '00afbfa3']]`

## 命令位置別の参照

- [`00afbe6c`](#insn-00afbe6c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbe70`](#insn-00afbe70) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbe74`](#insn-00afbe74) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbe78`](#insn-00afbe78) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbe7c`](#insn-00afbe7c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbe90`](#insn-00afbe90) → [`00bddb20`](../00bdd/00bddb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb20` · 推定シンボル `None` · 推定型 `None`
- [`00afbe98`](#insn-00afbe98) → [`00afbf7c`](#insn-00afbf7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbea0`](#insn-00afbea0) → [`00afbeac`](#insn-00afbeac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbea8`](#insn-00afbea8) → [`00afbf80`](#insn-00afbf80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbeb4`](#insn-00afbeb4) → [`00afbed0`](#insn-00afbed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbec8`](#insn-00afbec8) → [`00afbebc`](#insn-00afbebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbeec`](#insn-00afbeec) → [`00afbf20`](#insn-00afbf20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbf00`](#insn-00afbf00) → [`00afbef4`](#insn-00afbef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbf04`](#insn-00afbf04) → [`00afbf20`](#insn-00afbf20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbf1c`](#insn-00afbf1c) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00afbf24`](#insn-00afbf24) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00afbf2c`](#insn-00afbf2c) → [`00bddb30`](../00bdd/00bddb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb30` · 推定シンボル `None` · 推定型 `None`
- [`00afbf34`](#insn-00afbf34) → [`00bdeb40`](../00bde/00bdeb40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdeb40` · 推定シンボル `None` · 推定型 `None`
- [`00afbf40`](#insn-00afbf40) → [`00bddb20`](../00bdd/00bddb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb20` · 推定シンボル `None` · 推定型 `None`
- [`00afbf44`](#insn-00afbf44) → [`00afbea4`](#insn-00afbea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbf58`](#insn-00afbf58) → [`00afbf4c`](#insn-00afbf4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbf5c`](#insn-00afbf5c) → [`00afbea4`](#insn-00afbea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbf74`](#insn-00afbf74) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00afbf78`](#insn-00afbf78) → [`00afbea4`](#insn-00afbea4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbf84`](#insn-00afbf84) → [`00bddb30`](../00bdd/00bddb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb30` · 推定シンボル `None` · 推定型 `None`
- [`00afbf8c`](#insn-00afbf8c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbf90`](#insn-00afbf90) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbf94`](#insn-00afbf94) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbf98`](#insn-00afbf98) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afbe6c`](#insn-00afbe6c)

~~~json
{
  "source": "00afbe6c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbe70`](#insn-00afbe70)

~~~json
{
  "source": "00afbe70",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbe74`](#insn-00afbe74)

~~~json
{
  "source": "00afbe74",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbe78`](#insn-00afbe78)

~~~json
{
  "source": "00afbe78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbe7c`](#insn-00afbe7c)

~~~json
{
  "source": "00afbe7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbe90`](#insn-00afbe90)

~~~json
{
  "source": "00afbe90",
  "target": "00bddb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbe98`](#insn-00afbe98)

~~~json
{
  "source": "00afbe98",
  "target": "00afbf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbea0`](#insn-00afbea0)

~~~json
{
  "source": "00afbea0",
  "target": "00afbeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbea8`](#insn-00afbea8)

~~~json
{
  "source": "00afbea8",
  "target": "00afbf80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbeb4`](#insn-00afbeb4)

~~~json
{
  "source": "00afbeb4",
  "target": "00afbed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbec8`](#insn-00afbec8)

~~~json
{
  "source": "00afbec8",
  "target": "00afbebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbeec`](#insn-00afbeec)

~~~json
{
  "source": "00afbeec",
  "target": "00afbf20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbf00`](#insn-00afbf00)

~~~json
{
  "source": "00afbf00",
  "target": "00afbef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbf04`](#insn-00afbf04)

~~~json
{
  "source": "00afbf04",
  "target": "00afbf20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbf1c`](#insn-00afbf1c)

~~~json
{
  "source": "00afbf1c",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbf24`](#insn-00afbf24)

~~~json
{
  "source": "00afbf24",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbf2c`](#insn-00afbf2c)

~~~json
{
  "source": "00afbf2c",
  "target": "00bddb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbf34`](#insn-00afbf34)

~~~json
{
  "source": "00afbf34",
  "target": "00bdeb40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbf40`](#insn-00afbf40)

~~~json
{
  "source": "00afbf40",
  "target": "00bddb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbf44`](#insn-00afbf44)

~~~json
{
  "source": "00afbf44",
  "target": "00afbea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbf58`](#insn-00afbf58)

~~~json
{
  "source": "00afbf58",
  "target": "00afbf4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbf5c`](#insn-00afbf5c)

~~~json
{
  "source": "00afbf5c",
  "target": "00afbea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbf74`](#insn-00afbf74)

~~~json
{
  "source": "00afbf74",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbf78`](#insn-00afbf78)

~~~json
{
  "source": "00afbf78",
  "target": "00afbea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbf84`](#insn-00afbf84)

~~~json
{
  "source": "00afbf84",
  "target": "00bddb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbf8c`](#insn-00afbf8c)

~~~json
{
  "source": "00afbf8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbf90`](#insn-00afbf90)

~~~json
{
  "source": "00afbf90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbf94`](#insn-00afbf94)

~~~json
{
  "source": "00afbf94",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbf98`](#insn-00afbf98)

~~~json
{
  "source": "00afbf98",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
