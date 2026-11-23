# 00afbfa4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afc06c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc06c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-0e9859e6dd9b5829d7c5ea0d16355117)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afbfa4",
  "name": "_ZN8firebase8callback18CallbackDispatcherD2Ev",
  "size": 408,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f6900d42fd4446b3377be9c13c416cf9386ecf8dc2e25e41b13e3e8165a932f0",
  "source_text_sha256": "f6900d42fd4446b3377be9c13c416cf9386ecf8dc2e25e41b13e3e8165a932f0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afbfa4",
        "00afc13b"
      ]
    ],
    "bytes_sha256": "14d65c58b96ef0561e6d4befcd15eacf61facc293a0b2e61235b754183f2039d",
    "instruction_count": 102,
    "instruction_bytes": 408,
    "body_bytes": 408,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00bdeb80](../00bde/00bdeb80.md)

## 呼び出し先

- [00bdaf30](../00bda/00bdaf30.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)
- [00bddb50](../00bdd/00bddb50.md)
- [00bdde60](../00bdd/00bdde60.md)

## 関連文字列（未確認候補）

~~~text
"Callback dispatcher shut down with %d pending callbacks"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3223 bytes

~~~c

void _ZN8firebase8callback18CallbackDispatcherD2Ev(long *param_1)

{
  long *plVar1;
  long *plVar2;
  char cVar3;
  bool bVar4;
  long lVar5;
  long lVar6;
  long *plVar7;
  long *plVar8;
  
  plVar2 = param_1 + 3;
  _ZN8firebase5Mutex7AcquireEv(plVar2);
  if (param_1[2] != 0) {
    _ZN8firebase10LogWarningEPKcz("Callback dispatcher shut down with %d pending callbacks");
    lVar5 = param_1[2];
    while (lVar5 != 0) {
      lVar5 = *param_1;
      plVar7 = *(long **)(lVar5 + 0x18);
      *(undefined8 *)(lVar5 + 0x10) = 0;
      *(undefined8 *)(lVar5 + 0x18) = 0;
      if (plVar7 != (long *)0x0) {
        plVar8 = plVar7 + 1;
        do {
          lVar5 = *plVar8;
          cVar3 = '\x01';
          bVar4 = (bool)ExclusiveMonitorPass(plVar8,0x10);
          if (bVar4) {
            *plVar8 = lVar5 + -1;
            cVar3 = ExclusiveMonitorsStatus();
          }
        } while (cVar3 != '\0');
        if (lVar5 == 0) {
          (**(code **)(*plVar7 + 0x10))(plVar7);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
        }
      }
      plVar7 = (long *)*param_1;
      lVar5 = *plVar7;
      *(long *)(lVar5 + 8) = plVar7[1];
      *(long *)plVar7[1] = lVar5;
      param_1[2] = param_1[2] + -1;
      plVar8 = (long *)plVar7[3];
      if (plVar8 != (long *)0x0) {
        plVar1 = plVar8 + 1;
        do {
          lVar5 = *plVar1;
          cVar3 = '\x01';
          bVar4 = (bool)ExclusiveMonitorPass(plVar1,0x10);
          if (bVar4) {
            *plVar1 = lVar5 + -1;
            cVar3 = ExclusiveMonitorsStatus();
          }
        } while (cVar3 != '\0');
        if (lVar5 == 0) {
          (**(code **)(*plVar8 + 0x10))(plVar8);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
        }
      }
                    /* try { // try from 00afbfe8 to 00bfbfef has its CatchHandler @ 00b00380 */
      _ZdlPv(plVar7);
      lVar5 = param_1[2];
                    /* try { // try from 00afbff0 to 00bfc0eb has its CatchHandler @ 00af560c */
    }
  }
  _ZN8firebase5Mutex7ReleaseEv(plVar2);
  _ZN8firebase5MutexD1Ev(param_1 + 8);
  _ZN8firebase5MutexD1Ev(plVar2);
  if (param_1[2] != 0) {
    lVar5 = *param_1;
    plVar2 = (long *)param_1[1];
    lVar6 = *plVar2;
    *(undefined8 *)(lVar6 + 8) = *(undefined8 *)(lVar5 + 8);
    **(long **)(lVar5 + 8) = lVar6;
    param_1[2] = 0;
    while (plVar2 != param_1) {
                    /* try { // try from 00afc0ec to 00bfc10f has its CatchHandler @ 00b00450 */
      plVar7 = (long *)plVar2[3];
      plVar8 = (long *)plVar2[1];
      if (plVar7 != (long *)0x0) {
        plVar1 = plVar7 + 1;
        do {
          lVar5 = *plVar1;
          cVar3 = '\x01';
          bVar4 = (bool)ExclusiveMonitorPass(plVar1,0x10);
          if (bVar4) {
            *plVar1 = lVar5 + -1;
            cVar3 = ExclusiveMonitorsStatus();
          }
        } while (cVar3 != '\0');
        if (lVar5 == 0) {
                    /* try { // try from 00afc110 to 00bfc11b has its CatchHandler @ 00b003a4 */
          (**(code **)(*plVar7 + 0x10))(plVar7);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
        }
      }
      _ZdlPv(plVar2);
      plVar2 = plVar8;
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afbfa4"></a> `00afbfa4` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afbfa8"></a> `00afbfa8` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbfac"></a> `00afbfac` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afbfb0"></a> `00afbfb0` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00afbfb4"></a> `00afbfb4` | `14 60 00 91` | add x20,x0,#0x18 | `FALL_THROUGH`
<a id="insn-00afbfb8"></a> `00afbfb8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afbfbc"></a> `00afbfbc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afbfc0"></a> `00afbfc0` | `d8 86 03 94` | bl 0x00bddb20 | `UNCONDITIONAL_CALL`
<a id="insn-00afbfc4"></a> `00afbfc4` | `61 0a 40 f9` | ldr x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00afbfc8"></a> `00afbfc8` | `41 06 00 b4` | cbz x1,0x00afc090 | `CONDITIONAL_JUMP`
<a id="insn-00afbfcc"></a> `00afbfcc` | `00 bd ff d0` | adrp x0,0x29d000 | `FALL_THROUGH`
<a id="insn-00afbfd0"></a> `00afbfd0` | `00 c0 33 91` | add x0,x0,#0xcf0 | `FALL_THROUGH`
<a id="insn-00afbfd4"></a> `00afbfd4` | `a3 87 03 94` | bl 0x00bdde60 | `UNCONDITIONAL_CALL`
<a id="insn-00afbfd8"></a> `00afbfd8` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00afbfdc"></a> `00afbfdc` | `c8 00 00 b5` | cbnz x8,0x00afbff4 | `CONDITIONAL_JUMP`
<a id="insn-00afbfe0"></a> `00afbfe0` | `2c 00 00 14` | b 0x00afc090 | `UNCONDITIONAL_JUMP`
<a id="insn-00afbfe4"></a> `00afbfe4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afbfe8"></a> `00afbfe8` | `de 7b 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00afbfec"></a> `00afbfec` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00afbff0"></a> `00afbff0` | `08 05 00 b4` | cbz x8,0x00afc090 | `CONDITIONAL_JUMP`
<a id="insn-00afbff4"></a> `00afbff4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00afbff8"></a> `00afbff8` | `15 0d 40 f9` | ldr x21,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00afbffc"></a> `00afbffc` | `1f 7d 01 a9` | stp xzr,xzr,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00afc000"></a> `00afc000` | `b5 01 00 b4` | cbz x21,0x00afc034 | `CONDITIONAL_JUMP`
<a id="insn-00afc004"></a> `00afc004` | `a8 22 00 91` | add x8,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00afc008"></a> `00afc008` | `09 fd 5f c8` | ldaxr x9,[x8] | `FALL_THROUGH`
<a id="insn-00afc00c"></a> `00afc00c` | `2a 05 00 d1` | sub x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afc010"></a> `00afc010` | `0a fd 0b c8` | stlxr w11,x10,[x8] | `FALL_THROUGH`
<a id="insn-00afc014"></a> `00afc014` | `ab ff ff 35` | cbnz w11,0x00afc008 | `CONDITIONAL_JUMP`
<a id="insn-00afc018"></a> `00afc018` | `e9 00 00 b5` | cbnz x9,0x00afc034 | `CONDITIONAL_JUMP`
<a id="insn-00afc01c"></a> `00afc01c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00afc020"></a> `00afc020` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afc024"></a> `00afc024` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00afc028"></a> `00afc028` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afc02c"></a> `00afc02c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afc030"></a> `00afc030` | `c0 7b 03 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00afc034"></a> `00afc034` | `75 02 40 f9` | ldr x21,[x19] | `FALL_THROUGH`
<a id="insn-00afc038"></a> `00afc038` | `a8 26 40 a9` | ldp x8,x9,[x21] | `FALL_THROUGH`
<a id="insn-00afc03c"></a> `00afc03c` | `09 05 00 f9` | str x9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00afc040"></a> `00afc040` | `a9 06 40 f9` | ldr x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00afc044"></a> `00afc044` | `28 01 00 f9` | str x8,[x9] | `FALL_THROUGH`
<a id="insn-00afc048"></a> `00afc048` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00afc04c"></a> `00afc04c` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afc050"></a> `00afc050` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00afc054"></a> `00afc054` | `b6 0e 40 f9` | ldr x22,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00afc058"></a> `00afc058` | `76 fc ff b4` | cbz x22,0x00afbfe4 | `CONDITIONAL_JUMP`
<a id="insn-00afc05c"></a> `00afc05c` | `c8 22 00 91` | add x8,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00afc060"></a> `00afc060` | `09 fd 5f c8` | ldaxr x9,[x8] | `FALL_THROUGH`
<a id="insn-00afc064"></a> `00afc064` | `2a 05 00 d1` | sub x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afc068"></a> `00afc068` | `0a fd 0b c8` | stlxr w11,x10,[x8] | `FALL_THROUGH`
<a id="insn-00afc06c"></a> `00afc06c` | `ab ff ff 35` | cbnz w11,0x00afc060 | `CONDITIONAL_JUMP`
<a id="insn-00afc070"></a> `00afc070` | `a9 fb ff b5` | cbnz x9,0x00afbfe4 | `CONDITIONAL_JUMP`
<a id="insn-00afc074"></a> `00afc074` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00afc078"></a> `00afc078` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00afc07c"></a> `00afc07c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00afc080"></a> `00afc080` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afc084"></a> `00afc084` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00afc088"></a> `00afc088` | `aa 7b 03 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00afc08c"></a> `00afc08c` | `d6 ff ff 17` | b 0x00afbfe4 | `UNCONDITIONAL_JUMP`
<a id="insn-00afc090"></a> `00afc090` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afc094"></a> `00afc094` | `a7 86 03 94` | bl 0x00bddb30 | `UNCONDITIONAL_CALL`
<a id="insn-00afc098"></a> `00afc098` | `60 02 01 91` | add x0,x19,#0x40 | `FALL_THROUGH`
<a id="insn-00afc09c"></a> `00afc09c` | `ad 86 03 94` | bl 0x00bddb50 | `UNCONDITIONAL_CALL`
<a id="insn-00afc0a0"></a> `00afc0a0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afc0a4"></a> `00afc0a4` | `ab 86 03 94` | bl 0x00bddb50 | `UNCONDITIONAL_CALL`
<a id="insn-00afc0a8"></a> `00afc0a8` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00afc0ac"></a> `00afc0ac` | `08 04 00 b4` | cbz x8,0x00afc12c | `CONDITIONAL_JUMP`
<a id="insn-00afc0b0"></a> `00afc0b0` | `68 52 40 a9` | ldp x8,x20,[x19] | `FALL_THROUGH`
<a id="insn-00afc0b4"></a> `00afc0b4` | `09 05 40 f9` | ldr x9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00afc0b8"></a> `00afc0b8` | `8a 02 40 f9` | ldr x10,[x20] | `FALL_THROUGH`
<a id="insn-00afc0bc"></a> `00afc0bc` | `9f 02 13 eb` | cmp x20,x19 | `FALL_THROUGH`
<a id="insn-00afc0c0"></a> `00afc0c0` | `49 05 00 f9` | str x9,[x10, #0x8] | `FALL_THROUGH`
<a id="insn-00afc0c4"></a> `00afc0c4` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00afc0c8"></a> `00afc0c8` | `0a 01 00 f9` | str x10,[x8] | `FALL_THROUGH`
<a id="insn-00afc0cc"></a> `00afc0cc` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00afc0d0"></a> `00afc0d0` | `e1 00 00 54` | b.ne 0x00afc0ec | `CONDITIONAL_JUMP`
<a id="insn-00afc0d4"></a> `00afc0d4` | `16 00 00 14` | b 0x00afc12c | `UNCONDITIONAL_JUMP`
<a id="insn-00afc0d8"></a> `00afc0d8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afc0dc"></a> `00afc0dc` | `a1 7b 03 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00afc0e0"></a> `00afc0e0` | `df 02 13 eb` | cmp x22,x19 | `FALL_THROUGH`
<a id="insn-00afc0e4"></a> `00afc0e4` | `f4 03 16 aa` | mov x20,x22 | `FALL_THROUGH`
<a id="insn-00afc0e8"></a> `00afc0e8` | `20 02 00 54` | b.eq 0x00afc12c | `CONDITIONAL_JUMP`
<a id="insn-00afc0ec"></a> `00afc0ec` | `95 0e 40 f9` | ldr x21,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00afc0f0"></a> `00afc0f0` | `96 06 40 f9` | ldr x22,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00afc0f4"></a> `00afc0f4` | `35 ff ff b4` | cbz x21,0x00afc0d8 | `CONDITIONAL_JUMP`
<a id="insn-00afc0f8"></a> `00afc0f8` | `a8 22 00 91` | add x8,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00afc0fc"></a> `00afc0fc` | `09 fd 5f c8` | ldaxr x9,[x8] | `FALL_THROUGH`
<a id="insn-00afc100"></a> `00afc100` | `2a 05 00 d1` | sub x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00afc104"></a> `00afc104` | `0a fd 0b c8` | stlxr w11,x10,[x8] | `FALL_THROUGH`
<a id="insn-00afc108"></a> `00afc108` | `ab ff ff 35` | cbnz w11,0x00afc0fc | `CONDITIONAL_JUMP`
<a id="insn-00afc10c"></a> `00afc10c` | `69 fe ff b5` | cbnz x9,0x00afc0d8 | `CONDITIONAL_JUMP`
<a id="insn-00afc110"></a> `00afc110` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00afc114"></a> `00afc114` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afc118"></a> `00afc118` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00afc11c"></a> `00afc11c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afc120"></a> `00afc120` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afc124"></a> `00afc124` | `83 7b 03 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00afc128"></a> `00afc128` | `ec ff ff 17` | b 0x00afc0d8 | `UNCONDITIONAL_JUMP`
<a id="insn-00afc12c"></a> `00afc12c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afc130"></a> `00afc130` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afc134"></a> `00afc134` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afc138"></a> `00afc138` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afbfa4`](#insn-00afbfa4) 範囲 `[['00afbfa4', '00afbfcb']]`
  - `CONDITIONAL_JUMP` [`00afbfc8`](#insn-00afbfc8) → [`00afc090`](#insn-00afc090)
  - `FALL_THROUGH` [`00afbfc8`](#insn-00afbfc8) → [`00afbfcc`](#insn-00afbfcc)
- ブロック [`00afbfcc`](#insn-00afbfcc) 範囲 `[['00afbfcc', '00afbfdf']]`
  - `CONDITIONAL_JUMP` [`00afbfdc`](#insn-00afbfdc) → [`00afbff4`](#insn-00afbff4)
  - `FALL_THROUGH` [`00afbfdc`](#insn-00afbfdc) → [`00afbfe0`](#insn-00afbfe0)
- ブロック [`00afbfe0`](#insn-00afbfe0) 範囲 `[['00afbfe0', '00afbfe3']]`
  - `UNCONDITIONAL_JUMP` [`00afbfe0`](#insn-00afbfe0) → [`00afc090`](#insn-00afc090)
- ブロック [`00afbfe4`](#insn-00afbfe4) 範囲 `[['00afbfe4', '00afbfe7']]`
  - `FALL_THROUGH` [`00afbfe4`](#insn-00afbfe4) → [`00afbfe8`](#insn-00afbfe8)
- ブロック [`00afbfe8`](#insn-00afbfe8) 範囲 `[['00afbfe8', '00afbfef']]`
  - `FALL_THROUGH` [`00afbfec`](#insn-00afbfec) → [`00afbff0`](#insn-00afbff0)
- ブロック [`00afbff0`](#insn-00afbff0) 範囲 `[['00afbff0', '00afbff3']]`
  - `CONDITIONAL_JUMP` [`00afbff0`](#insn-00afbff0) → [`00afc090`](#insn-00afc090)
  - `FALL_THROUGH` [`00afbff0`](#insn-00afbff0) → [`00afbff4`](#insn-00afbff4)
- ブロック [`00afbff4`](#insn-00afbff4) 範囲 `[['00afbff4', '00afc003']]`
  - `CONDITIONAL_JUMP` [`00afc000`](#insn-00afc000) → [`00afc034`](#insn-00afc034)
  - `FALL_THROUGH` [`00afc000`](#insn-00afc000) → [`00afc004`](#insn-00afc004)
- ブロック [`00afc004`](#insn-00afc004) 範囲 `[['00afc004', '00afc007']]`
  - `FALL_THROUGH` [`00afc004`](#insn-00afc004) → [`00afc008`](#insn-00afc008)
- ブロック [`00afc008`](#insn-00afc008) 範囲 `[['00afc008', '00afc017']]`
  - `CONDITIONAL_JUMP` [`00afc014`](#insn-00afc014) → [`00afc008`](#insn-00afc008)
  - `FALL_THROUGH` [`00afc014`](#insn-00afc014) → [`00afc018`](#insn-00afc018)
- ブロック [`00afc018`](#insn-00afc018) 範囲 `[['00afc018', '00afc01b']]`
  - `CONDITIONAL_JUMP` [`00afc018`](#insn-00afc018) → [`00afc034`](#insn-00afc034)
  - `FALL_THROUGH` [`00afc018`](#insn-00afc018) → [`00afc01c`](#insn-00afc01c)
- ブロック [`00afc01c`](#insn-00afc01c) 範囲 `[['00afc01c', '00afc033']]`
  - `FALL_THROUGH` [`00afc030`](#insn-00afc030) → [`00afc034`](#insn-00afc034)
- ブロック [`00afc034`](#insn-00afc034) 範囲 `[['00afc034', '00afc05b']]`
  - `CONDITIONAL_JUMP` [`00afc058`](#insn-00afc058) → [`00afbfe4`](#insn-00afbfe4)
  - `FALL_THROUGH` [`00afc058`](#insn-00afc058) → [`00afc05c`](#insn-00afc05c)
- ブロック [`00afc05c`](#insn-00afc05c) 範囲 `[['00afc05c', '00afc05f']]`
  - `FALL_THROUGH` [`00afc05c`](#insn-00afc05c) → [`00afc060`](#insn-00afc060)
- ブロック [`00afc060`](#insn-00afc060) 範囲 `[['00afc060', '00afc06f']]`
  - `CONDITIONAL_JUMP` [`00afc06c`](#insn-00afc06c) → [`00afc060`](#insn-00afc060)
  - `FALL_THROUGH` [`00afc06c`](#insn-00afc06c) → [`00afc070`](#insn-00afc070)
- ブロック [`00afc070`](#insn-00afc070) 範囲 `[['00afc070', '00afc073']]`
  - `CONDITIONAL_JUMP` [`00afc070`](#insn-00afc070) → [`00afbfe4`](#insn-00afbfe4)
  - `FALL_THROUGH` [`00afc070`](#insn-00afc070) → [`00afc074`](#insn-00afc074)
- ブロック [`00afc074`](#insn-00afc074) 範囲 `[['00afc074', '00afc08f']]`
  - `UNCONDITIONAL_JUMP` [`00afc08c`](#insn-00afc08c) → [`00afbfe4`](#insn-00afbfe4)
- ブロック [`00afc090`](#insn-00afc090) 範囲 `[['00afc090', '00afc0af']]`
  - `CONDITIONAL_JUMP` [`00afc0ac`](#insn-00afc0ac) → [`00afc12c`](#insn-00afc12c)
  - `FALL_THROUGH` [`00afc0ac`](#insn-00afc0ac) → [`00afc0b0`](#insn-00afc0b0)
- ブロック [`00afc0b0`](#insn-00afc0b0) 範囲 `[['00afc0b0', '00afc0d3']]`
  - `CONDITIONAL_JUMP` [`00afc0d0`](#insn-00afc0d0) → [`00afc0ec`](#insn-00afc0ec)
  - `FALL_THROUGH` [`00afc0d0`](#insn-00afc0d0) → [`00afc0d4`](#insn-00afc0d4)
- ブロック [`00afc0d4`](#insn-00afc0d4) 範囲 `[['00afc0d4', '00afc0d7']]`
  - `UNCONDITIONAL_JUMP` [`00afc0d4`](#insn-00afc0d4) → [`00afc12c`](#insn-00afc12c)
- ブロック [`00afc0d8`](#insn-00afc0d8) 範囲 `[['00afc0d8', '00afc0eb']]`
  - `CONDITIONAL_JUMP` [`00afc0e8`](#insn-00afc0e8) → [`00afc12c`](#insn-00afc12c)
  - `FALL_THROUGH` [`00afc0e8`](#insn-00afc0e8) → [`00afc0ec`](#insn-00afc0ec)
- ブロック [`00afc0ec`](#insn-00afc0ec) 範囲 `[['00afc0ec', '00afc0f7']]`
  - `CONDITIONAL_JUMP` [`00afc0f4`](#insn-00afc0f4) → [`00afc0d8`](#insn-00afc0d8)
  - `FALL_THROUGH` [`00afc0f4`](#insn-00afc0f4) → [`00afc0f8`](#insn-00afc0f8)
- ブロック [`00afc0f8`](#insn-00afc0f8) 範囲 `[['00afc0f8', '00afc0fb']]`
  - `FALL_THROUGH` [`00afc0f8`](#insn-00afc0f8) → [`00afc0fc`](#insn-00afc0fc)
- ブロック [`00afc0fc`](#insn-00afc0fc) 範囲 `[['00afc0fc', '00afc10b']]`
  - `CONDITIONAL_JUMP` [`00afc108`](#insn-00afc108) → [`00afc0fc`](#insn-00afc0fc)
  - `FALL_THROUGH` [`00afc108`](#insn-00afc108) → [`00afc10c`](#insn-00afc10c)
- ブロック [`00afc10c`](#insn-00afc10c) 範囲 `[['00afc10c', '00afc10f']]`
  - `CONDITIONAL_JUMP` [`00afc10c`](#insn-00afc10c) → [`00afc0d8`](#insn-00afc0d8)
  - `FALL_THROUGH` [`00afc10c`](#insn-00afc10c) → [`00afc110`](#insn-00afc110)
- ブロック [`00afc110`](#insn-00afc110) 範囲 `[['00afc110', '00afc12b']]`
  - `UNCONDITIONAL_JUMP` [`00afc128`](#insn-00afc128) → [`00afc0d8`](#insn-00afc0d8)
- ブロック [`00afc12c`](#insn-00afc12c) 範囲 `[['00afc12c', '00afc13b']]`

## 命令位置別の参照

- [`00afbfa4`](#insn-00afbfa4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbfa8`](#insn-00afbfa8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbfac`](#insn-00afbfac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbfc0`](#insn-00afbfc0) → [`00bddb20`](../00bdd/00bddb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb20` · 推定シンボル `None` · 推定型 `None`
- [`00afbfc8`](#insn-00afbfc8) → [`00afc090`](#insn-00afc090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbfd0`](#insn-00afbfd0) → `0029dcf0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00afbfd4`](#insn-00afbfd4) → [`00bdde60`](../00bdd/00bdde60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdde60` · 推定シンボル `None` · 推定型 `None`
- [`00afbfdc`](#insn-00afbfdc) → [`00afbff4`](#insn-00afbff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbfe0`](#insn-00afbfe0) → [`00afc090`](#insn-00afc090) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbfe8`](#insn-00afbfe8) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00afbff0`](#insn-00afbff0) → [`00afc090`](#insn-00afc090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc000`](#insn-00afc000) → [`00afc034`](#insn-00afc034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc014`](#insn-00afc014) → [`00afc008`](#insn-00afc008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc018`](#insn-00afc018) → [`00afc034`](#insn-00afc034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc030`](#insn-00afc030) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00afc058`](#insn-00afc058) → [`00afbfe4`](#insn-00afbfe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc06c`](#insn-00afc06c) → [`00afc060`](#insn-00afc060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc070`](#insn-00afc070) → [`00afbfe4`](#insn-00afbfe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc088`](#insn-00afc088) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00afc08c`](#insn-00afc08c) → [`00afbfe4`](#insn-00afbfe4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc094`](#insn-00afc094) → [`00bddb30`](../00bdd/00bddb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb30` · 推定シンボル `None` · 推定型 `None`
- [`00afc09c`](#insn-00afc09c) → [`00bddb50`](../00bdd/00bddb50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb50` · 推定シンボル `None` · 推定型 `None`
- [`00afc0a4`](#insn-00afc0a4) → [`00bddb50`](../00bdd/00bddb50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb50` · 推定シンボル `None` · 推定型 `None`
- [`00afc0ac`](#insn-00afc0ac) → [`00afc12c`](#insn-00afc12c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc0d0`](#insn-00afc0d0) → [`00afc0ec`](#insn-00afc0ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc0d4`](#insn-00afc0d4) → [`00afc12c`](#insn-00afc12c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc0dc`](#insn-00afc0dc) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00afc0e8`](#insn-00afc0e8) → [`00afc12c`](#insn-00afc12c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc0f4`](#insn-00afc0f4) → [`00afc0d8`](#insn-00afc0d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc108`](#insn-00afc108) → [`00afc0fc`](#insn-00afc0fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc10c`](#insn-00afc10c) → [`00afc0d8`](#insn-00afc0d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc124`](#insn-00afc124) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00afc128`](#insn-00afc128) → [`00afc0d8`](#insn-00afc0d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc12c`](#insn-00afc12c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc130`](#insn-00afc130) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afbfa4`](#insn-00afbfa4)

~~~json
{
  "source": "00afbfa4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbfa8`](#insn-00afbfa8)

~~~json
{
  "source": "00afbfa8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbfac`](#insn-00afbfac)

~~~json
{
  "source": "00afbfac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbfc0`](#insn-00afbfc0)

~~~json
{
  "source": "00afbfc0",
  "target": "00bddb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbfc8`](#insn-00afbfc8)

~~~json
{
  "source": "00afbfc8",
  "target": "00afc090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbfd0`](#insn-00afbfd0)

~~~json
{
  "source": "00afbfd0",
  "target": "0029dcf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029dcf0",
  "offset": 0,
  "size": 56,
  "datatype": "string",
  "bytes": "43616c6c6261636b2064697370617463686572207368757420646f776e207769",
  "capture_start": "0029dcf0",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afbfd4`](#insn-00afbfd4)

~~~json
{
  "source": "00afbfd4",
  "target": "00bdde60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbfdc`](#insn-00afbfdc)

~~~json
{
  "source": "00afbfdc",
  "target": "00afbff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbfe0`](#insn-00afbfe0)

~~~json
{
  "source": "00afbfe0",
  "target": "00afc090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbfe8`](#insn-00afbfe8)

~~~json
{
  "source": "00afbfe8",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbff0`](#insn-00afbff0)

~~~json
{
  "source": "00afbff0",
  "target": "00afc090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc000`](#insn-00afc000)

~~~json
{
  "source": "00afc000",
  "target": "00afc034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc014`](#insn-00afc014)

~~~json
{
  "source": "00afc014",
  "target": "00afc008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc018`](#insn-00afc018)

~~~json
{
  "source": "00afc018",
  "target": "00afc034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc030`](#insn-00afc030)

~~~json
{
  "source": "00afc030",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc058`](#insn-00afc058)

~~~json
{
  "source": "00afc058",
  "target": "00afbfe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc06c`](#insn-00afc06c)

~~~json
{
  "source": "00afc06c",
  "target": "00afc060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc070`](#insn-00afc070)

~~~json
{
  "source": "00afc070",
  "target": "00afbfe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc088`](#insn-00afc088)

~~~json
{
  "source": "00afc088",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc08c`](#insn-00afc08c)

~~~json
{
  "source": "00afc08c",
  "target": "00afbfe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc094`](#insn-00afc094)

~~~json
{
  "source": "00afc094",
  "target": "00bddb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc09c`](#insn-00afc09c)

~~~json
{
  "source": "00afc09c",
  "target": "00bddb50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc0a4`](#insn-00afc0a4)

~~~json
{
  "source": "00afc0a4",
  "target": "00bddb50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc0ac`](#insn-00afc0ac)

~~~json
{
  "source": "00afc0ac",
  "target": "00afc12c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc0d0`](#insn-00afc0d0)

~~~json
{
  "source": "00afc0d0",
  "target": "00afc0ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc0d4`](#insn-00afc0d4)

~~~json
{
  "source": "00afc0d4",
  "target": "00afc12c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc0dc`](#insn-00afc0dc)

~~~json
{
  "source": "00afc0dc",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc0e8`](#insn-00afc0e8)

~~~json
{
  "source": "00afc0e8",
  "target": "00afc12c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc0f4`](#insn-00afc0f4)

~~~json
{
  "source": "00afc0f4",
  "target": "00afc0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc108`](#insn-00afc108)

~~~json
{
  "source": "00afc108",
  "target": "00afc0fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc10c`](#insn-00afc10c)

~~~json
{
  "source": "00afc10c",
  "target": "00afc0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc124`](#insn-00afc124)

~~~json
{
  "source": "00afc124",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc128`](#insn-00afc128)

~~~json
{
  "source": "00afc128",
  "target": "00afc0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc12c`](#insn-00afc12c)

~~~json
{
  "source": "00afc12c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc130`](#insn-00afc130)

~~~json
{
  "source": "00afc130",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
