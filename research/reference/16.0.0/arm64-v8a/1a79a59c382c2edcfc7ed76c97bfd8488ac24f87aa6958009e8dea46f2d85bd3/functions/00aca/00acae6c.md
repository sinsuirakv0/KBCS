# 00acae6c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a6ced8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6ced8.md) · 移動量 `+0x5df94`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0018.md#compare-a7b3be450521870161f8e8607b8f2a1e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acb068`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb068.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0035.md#compare-eb32c13b6b1daa4faa2d94e44e8a9dce)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acae6c",
  "name": "FUN_00acae6c",
  "size": 356,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "737d424504a011beac9eed20cf2fdc142952e6ce00156f809347e603ebb48681",
  "source_text_sha256": "737d424504a011beac9eed20cf2fdc142952e6ce00156f809347e603ebb48681",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acae6c",
        "00acafcf"
      ]
    ],
    "bytes_sha256": "ea4e443a87802e85fefd6912dbe633b4754504cd6e349963922574728f4ccdba",
    "instruction_count": 89,
    "instruction_bytes": 356,
    "body_bytes": 356,
    "indirect": 10,
    "unresolved": 10
  }
}
~~~

## 呼び出し元

- [00ac87ac](../00ac8/00ac87ac.md)
- [00ac923c](../00ac9/00ac923c.md)

## 呼び出し先

- [00c57ae0](../00c57/00c57ae0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1450 bytes

~~~c

void FUN_00acae6c(long *param_1,long *param_2)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  long local_60 [5];
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  if (param_2 != param_1) {
    plVar2 = (long *)param_1[4];
    plVar3 = (long *)param_2[4];
    if (plVar2 == param_1) {
      if (plVar3 == param_2) {
        (**(code **)(*param_1 + 0x18))(param_1,local_60);
        (**(code **)(*(long *)param_1[4] + 0x20))();
        param_1[4] = 0;
        (**(code **)(*(long *)param_2[4] + 0x18))((long *)param_2[4],param_1);
        (**(code **)(*(long *)param_2[4] + 0x20))();
        param_2[4] = 0;
        param_1[4] = (long)param_1;
        (**(code **)(local_60[0] + 0x18))(local_60,param_2);
        (**(code **)(local_60[0] + 0x20))(local_60);
      }
      else {
        (**(code **)(*param_1 + 0x18))(param_1,param_2);
        (**(code **)(*(long *)param_1[4] + 0x20))();
        param_1[4] = param_2[4];
      }
      param_2[4] = (long)param_2;
    }
    else if (plVar3 == param_2) {
      (**(code **)(*param_2 + 0x18))(param_2,param_1);
      (**(code **)(*(long *)param_2[4] + 0x20))();
      param_2[4] = param_1[4];
      param_1[4] = (long)param_1;
    }
    else {
      param_1[4] = (long)plVar3;
      param_2[4] = (long)plVar2;
    }
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
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
<a id="insn-00acae6c"></a> `00acae6c` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acae70"></a> `00acae70` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acae74"></a> `00acae74` | `f5 23 00 f9` | str x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acae78"></a> `00acae78` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acae7c"></a> `00acae7c` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00acae80"></a> `00acae80` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acae84"></a> `00acae84` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acae88"></a> `00acae88` | `3f 00 00 eb` | cmp x1,x0 | `FALL_THROUGH`
<a id="insn-00acae8c"></a> `00acae8c` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acae90"></a> `00acae90` | `c0 08 00 54` | b.eq 0x00acafa8 | `CONDITIONAL_JUMP`
<a id="insn-00acae94"></a> `00acae94` | `08 10 40 f9` | ldr x8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00acae98"></a> `00acae98` | `29 10 40 f9` | ldr x9,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00acae9c"></a> `00acae9c` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00acaea0"></a> `00acaea0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acaea4"></a> `00acaea4` | `1f 01 00 eb` | cmp x8,x0 | `FALL_THROUGH`
<a id="insn-00acaea8"></a> `00acaea8` | `c0 00 00 54` | b.eq 0x00acaec0 | `CONDITIONAL_JUMP`
<a id="insn-00acaeac"></a> `00acaeac` | `3f 01 13 eb` | cmp x9,x19 | `FALL_THROUGH`
<a id="insn-00acaeb0"></a> `00acaeb0` | `40 02 00 54` | b.eq 0x00acaef8 | `CONDITIONAL_JUMP`
<a id="insn-00acaeb4"></a> `00acaeb4` | `89 12 00 f9` | str x9,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00acaeb8"></a> `00acaeb8` | `68 12 00 f9` | str x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00acaebc"></a> `00acaebc` | `3b 00 00 14` | b 0x00acafa8 | `UNCONDITIONAL_JUMP`
<a id="insn-00acaec0"></a> `00acaec0` | `3f 01 13 eb` | cmp x9,x19 | `FALL_THROUGH`
<a id="insn-00acaec4"></a> `00acaec4` | `40 03 00 54` | b.eq 0x00acaf2c | `CONDITIONAL_JUMP`
<a id="insn-00acaec8"></a> `00acaec8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00acaecc"></a> `00acaecc` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00acaed0"></a> `00acaed0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acaed4"></a> `00acaed4` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00acaed8"></a> `00acaed8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acaedc"></a> `00acaedc` | `80 12 40 f9` | ldr x0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00acaee0"></a> `00acaee0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acaee4"></a> `00acaee4` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00acaee8"></a> `00acaee8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acaeec"></a> `00acaeec` | `68 12 40 f9` | ldr x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00acaef0"></a> `00acaef0` | `88 12 00 f9` | str x8,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00acaef4"></a> `00acaef4` | `2c 00 00 14` | b 0x00acafa4 | `UNCONDITIONAL_JUMP`
<a id="insn-00acaef8"></a> `00acaef8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00acaefc"></a> `00acaefc` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00acaf00"></a> `00acaf00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acaf04"></a> `00acaf04` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00acaf08"></a> `00acaf08` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acaf0c"></a> `00acaf0c` | `60 12 40 f9` | ldr x0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00acaf10"></a> `00acaf10` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acaf14"></a> `00acaf14` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00acaf18"></a> `00acaf18` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acaf1c"></a> `00acaf1c` | `88 12 40 f9` | ldr x8,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00acaf20"></a> `00acaf20` | `68 12 00 f9` | str x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00acaf24"></a> `00acaf24` | `94 12 00 f9` | str x20,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00acaf28"></a> `00acaf28` | `20 00 00 14` | b 0x00acafa8 | `UNCONDITIONAL_JUMP`
<a id="insn-00acaf2c"></a> `00acaf2c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00acaf30"></a> `00acaf30` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00acaf34"></a> `00acaf34` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00acaf38"></a> `00acaf38` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acaf3c"></a> `00acaf3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acaf40"></a> `00acaf40` | `80 12 40 f9` | ldr x0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00acaf44"></a> `00acaf44` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acaf48"></a> `00acaf48` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00acaf4c"></a> `00acaf4c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acaf50"></a> `00acaf50` | `9f 12 00 f9` | str xzr,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00acaf54"></a> `00acaf54` | `60 12 40 f9` | ldr x0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00acaf58"></a> `00acaf58` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acaf5c"></a> `00acaf5c` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00acaf60"></a> `00acaf60` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00acaf64"></a> `00acaf64` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acaf68"></a> `00acaf68` | `60 12 40 f9` | ldr x0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00acaf6c"></a> `00acaf6c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acaf70"></a> `00acaf70` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00acaf74"></a> `00acaf74` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acaf78"></a> `00acaf78` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00acaf7c"></a> `00acaf7c` | `7f 12 00 f9` | str xzr,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00acaf80"></a> `00acaf80` | `94 12 00 f9` | str x20,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00acaf84"></a> `00acaf84` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00acaf88"></a> `00acaf88` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00acaf8c"></a> `00acaf8c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00acaf90"></a> `00acaf90` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acaf94"></a> `00acaf94` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00acaf98"></a> `00acaf98` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00acaf9c"></a> `00acaf9c` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00acafa0"></a> `00acafa0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acafa4"></a> `00acafa4` | `73 12 00 f9` | str x19,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00acafa8"></a> `00acafa8` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acafac"></a> `00acafac` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acafb0"></a> `00acafb0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acafb4"></a> `00acafb4` | `c1 00 00 54` | b.ne 0x00acafcc | `CONDITIONAL_JUMP`
<a id="insn-00acafb8"></a> `00acafb8` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acafbc"></a> `00acafbc` | `f5 23 40 f9` | ldr x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acafc0"></a> `00acafc0` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acafc4"></a> `00acafc4` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acafc8"></a> `00acafc8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acafcc"></a> `00acafcc` | `c5 32 06 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acae6c`](#insn-00acae6c) 範囲 `[['00acae6c', '00acae93']]`
  - `CONDITIONAL_JUMP` [`00acae90`](#insn-00acae90) → [`00acafa8`](#insn-00acafa8)
  - `FALL_THROUGH` [`00acae90`](#insn-00acae90) → [`00acae94`](#insn-00acae94)
- ブロック [`00acae94`](#insn-00acae94) 範囲 `[['00acae94', '00acaeab']]`
  - `CONDITIONAL_JUMP` [`00acaea8`](#insn-00acaea8) → [`00acaec0`](#insn-00acaec0)
  - `FALL_THROUGH` [`00acaea8`](#insn-00acaea8) → [`00acaeac`](#insn-00acaeac)
- ブロック [`00acaeac`](#insn-00acaeac) 範囲 `[['00acaeac', '00acaeb3']]`
  - `CONDITIONAL_JUMP` [`00acaeb0`](#insn-00acaeb0) → [`00acaef8`](#insn-00acaef8)
  - `FALL_THROUGH` [`00acaeb0`](#insn-00acaeb0) → [`00acaeb4`](#insn-00acaeb4)
- ブロック [`00acaeb4`](#insn-00acaeb4) 範囲 `[['00acaeb4', '00acaebf']]`
  - `UNCONDITIONAL_JUMP` [`00acaebc`](#insn-00acaebc) → [`00acafa8`](#insn-00acafa8)
- ブロック [`00acaec0`](#insn-00acaec0) 範囲 `[['00acaec0', '00acaec7']]`
  - `CONDITIONAL_JUMP` [`00acaec4`](#insn-00acaec4) → [`00acaf2c`](#insn-00acaf2c)
  - `FALL_THROUGH` [`00acaec4`](#insn-00acaec4) → [`00acaec8`](#insn-00acaec8)
- ブロック [`00acaec8`](#insn-00acaec8) 範囲 `[['00acaec8', '00acaef7']]`
  - `UNCONDITIONAL_JUMP` [`00acaef4`](#insn-00acaef4) → [`00acafa4`](#insn-00acafa4)
- ブロック [`00acaef8`](#insn-00acaef8) 範囲 `[['00acaef8', '00acaf2b']]`
  - `UNCONDITIONAL_JUMP` [`00acaf28`](#insn-00acaf28) → [`00acafa8`](#insn-00acafa8)
- ブロック [`00acaf2c`](#insn-00acaf2c) 範囲 `[['00acaf2c', '00acafa3']]`
  - `FALL_THROUGH` [`00acafa0`](#insn-00acafa0) → [`00acafa4`](#insn-00acafa4)
- ブロック [`00acafa4`](#insn-00acafa4) 範囲 `[['00acafa4', '00acafa7']]`
  - `FALL_THROUGH` [`00acafa4`](#insn-00acafa4) → [`00acafa8`](#insn-00acafa8)
- ブロック [`00acafa8`](#insn-00acafa8) 範囲 `[['00acafa8', '00acafb7']]`
  - `CONDITIONAL_JUMP` [`00acafb4`](#insn-00acafb4) → [`00acafcc`](#insn-00acafcc)
  - `FALL_THROUGH` [`00acafb4`](#insn-00acafb4) → [`00acafb8`](#insn-00acafb8)
- ブロック [`00acafb8`](#insn-00acafb8) 範囲 `[['00acafb8', '00acafcb']]`
- ブロック [`00acafcc`](#insn-00acafcc) 範囲 `[['00acafcc', '00acafcf']]`

## 命令位置別の参照

- [`00acae70`](#insn-00acae70) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae74`](#insn-00acae74) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae78`](#insn-00acae78) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae8c`](#insn-00acae8c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acae90`](#insn-00acae90) → [`00acafa8`](#insn-00acafa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaea8`](#insn-00acaea8) → [`00acaec0`](#insn-00acaec0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaeb0`](#insn-00acaeb0) → [`00acaef8`](#insn-00acaef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaebc`](#insn-00acaebc) → [`00acafa8`](#insn-00acafa8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaec4`](#insn-00acaec4) → [`00acaf2c`](#insn-00acaf2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaef4`](#insn-00acaef4) → [`00acafa4`](#insn-00acafa4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaf28`](#insn-00acaf28) → [`00acafa8`](#insn-00acafa8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaf78`](#insn-00acaf78) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaf94`](#insn-00acaf94) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acafac`](#insn-00acafac) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acafb4`](#insn-00acafb4) → [`00acafcc`](#insn-00acafcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acafb8`](#insn-00acafb8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acafbc`](#insn-00acafbc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acafc0`](#insn-00acafc0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acafcc`](#insn-00acafcc) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acae70`](#insn-00acae70)

~~~json
{
  "source": "00acae70",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae74`](#insn-00acae74)

~~~json
{
  "source": "00acae74",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae78`](#insn-00acae78)

~~~json
{
  "source": "00acae78",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae8c`](#insn-00acae8c)

~~~json
{
  "source": "00acae8c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acae90`](#insn-00acae90)

~~~json
{
  "source": "00acae90",
  "target": "00acafa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaea8`](#insn-00acaea8)

~~~json
{
  "source": "00acaea8",
  "target": "00acaec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaeb0`](#insn-00acaeb0)

~~~json
{
  "source": "00acaeb0",
  "target": "00acaef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaebc`](#insn-00acaebc)

~~~json
{
  "source": "00acaebc",
  "target": "00acafa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaec4`](#insn-00acaec4)

~~~json
{
  "source": "00acaec4",
  "target": "00acaf2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaef4`](#insn-00acaef4)

~~~json
{
  "source": "00acaef4",
  "target": "00acafa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaf28`](#insn-00acaf28)

~~~json
{
  "source": "00acaf28",
  "target": "00acafa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaf78`](#insn-00acaf78)

~~~json
{
  "source": "00acaf78",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaf94`](#insn-00acaf94)

~~~json
{
  "source": "00acaf94",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acafac`](#insn-00acafac)

~~~json
{
  "source": "00acafac",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acafb4`](#insn-00acafb4)

~~~json
{
  "source": "00acafb4",
  "target": "00acafcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acafb8`](#insn-00acafb8)

~~~json
{
  "source": "00acafb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acafbc`](#insn-00acafbc)

~~~json
{
  "source": "00acafbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acafc0`](#insn-00acafc0)

~~~json
{
  "source": "00acafc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acafcc`](#insn-00acafcc)

~~~json
{
  "source": "00acafcc",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
