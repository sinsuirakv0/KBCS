# 00bfaf1c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7e4d4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e4d4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0072.md#compare-9853a6076ea03cb983c1745b6bdc775c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfb344`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb344.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-7fc752b7de7f137a85f548153d788a32)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfaf1c",
  "name": "_ZNSt6__ndk18ios_base17register_callbackEPFvNS0_5eventERS0_iEi",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0d97e7813080c2b530a8c5308607e3e3aaf563ead907a5794d1b5560e0f55648",
  "source_text_sha256": "0d97e7813080c2b530a8c5308607e3e3aaf563ead907a5794d1b5560e0f55648",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfaf1c",
        "00bfaffb"
      ]
    ],
    "bytes_sha256": "d8ebccb59a00e5e60cf514e7fd45d1917271504770233ed8b9c39065aedb64e5",
    "instruction_count": 56,
    "instruction_bytes": 224,
    "body_bytes": 224,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bfb11c](../00bfb/00bfb11c.md)
- [00c59ca0](../00c59/00c59ca0.md)

## 関連文字列（未確認候補）

~~~text
"ios_base::clear"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1511 bytes

~~~c

void _ZNSt6__ndk18ios_base17register_callbackEPFvNS0_5eventERS0_iEi
               (long param_1,undefined8 param_2,undefined4 param_3)

{
  uint uVar1;
  void *pvVar2;
  ulong uVar3;
  ulong uVar4;
  long lVar5;
  
  lVar5 = *(long *)(param_1 + 0x48);
  uVar3 = lVar5 + 1;
  if (*(ulong *)(param_1 + 0x50) < uVar3) {
    uVar4 = *(ulong *)(param_1 + 0x50) * 2;
    if (uVar4 < uVar3 || uVar4 - uVar3 == 0) {
      uVar4 = uVar3;
    }
    if (0xffffffffffffffe < uVar3) {
      uVar4 = 0x1fffffffffffffff;
    }
    pvVar2 = realloc(*(void **)(param_1 + 0x38),uVar4 << 3);
    if (pvVar2 == (void *)0x0) {
      uVar1 = *(uint *)(param_1 + 0x20) | 1;
      *(uint *)(param_1 + 0x20) = uVar1;
      if ((*(uint *)(param_1 + 0x24) & uVar1) != 0) goto LAB_00bfaff0;
    }
    *(void **)(param_1 + 0x38) = pvVar2;
    pvVar2 = realloc(*(void **)(param_1 + 0x40),uVar4 << 2);
    if (pvVar2 == (void *)0x0) {
      uVar1 = *(uint *)(param_1 + 0x20) | 1;
      *(uint *)(param_1 + 0x20) = uVar1;
      if ((*(uint *)(param_1 + 0x24) & uVar1) != 0) {
LAB_00bfaff0:
                    /* WARNING: Subroutine does not return */
        FUN_00bfb11c("ios_base::clear");
      }
    }
    lVar5 = *(long *)(param_1 + 0x48);
    *(void **)(param_1 + 0x40) = pvVar2;
    *(ulong *)(param_1 + 0x50) = uVar4;
    uVar3 = lVar5 + 1;
  }
  *(undefined8 *)(*(long *)(param_1 + 0x38) + lVar5 * 8) = param_2;
  *(undefined4 *)(*(long *)(param_1 + 0x40) + lVar5 * 4) = param_3;
  *(ulong *)(param_1 + 0x48) = uVar3;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfaf1c"></a> `00bfaf1c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfaf20"></a> `00bfaf20` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bfaf24"></a> `00bfaf24` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfaf28"></a> `00bfaf28` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfaf2c"></a> `00bfaf2c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfaf30"></a> `00bfaf30` | `09 a8 44 a9` | ldp x9,x10,[x0, #0x48] | `FALL_THROUGH`
<a id="insn-00bfaf34"></a> `00bfaf34` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00bfaf38"></a> `00bfaf38` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bfaf3c"></a> `00bfaf3c` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bfaf40"></a> `00bfaf40` | `28 05 00 91` | add x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bfaf44"></a> `00bfaf44` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00bfaf48"></a> `00bfaf48` | `09 04 00 54` | b.ls 0x00bfafc8 | `CONDITIONAL_JUMP`
<a id="insn-00bfaf4c"></a> `00bfaf4c` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bfaf50"></a> `00bfaf50` | `0a 00 fe 92` | mov x10,#0xfffffffffffffff | `FALL_THROUGH`
<a id="insn-00bfaf54"></a> `00bfaf54` | `80 1e 40 f9` | ldr x0,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00bfaf58"></a> `00bfaf58` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bfaf5c"></a> `00bfaf5c` | `29 81 88 9a` | csel x9,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bfaf60"></a> `00bfaf60` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00bfaf64"></a> `00bfaf64` | `08 00 fc 92` | mov x8,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bfaf68"></a> `00bfaf68` | `36 31 88 9a` | csel x22,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00bfaf6c"></a> `00bfaf6c` | `c1 f2 7d d3` | lsl x1,x22,#0x3 | `FALL_THROUGH`
<a id="insn-00bfaf70"></a> `00bfaf70` | `4c 7b 01 94` | bl 0x00c59ca0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfaf74"></a> `00bfaf74` | `c0 00 00 b5` | cbnz x0,0x00bfaf8c | `CONDITIONAL_JUMP`
<a id="insn-00bfaf78"></a> `00bfaf78` | `88 26 44 29` | ldp w8,w9,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bfaf7c"></a> `00bfaf7c` | `08 01 00 32` | orr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfaf80"></a> `00bfaf80` | `3f 01 08 6a` | tst w9,w8 | `FALL_THROUGH`
<a id="insn-00bfaf84"></a> `00bfaf84` | `88 22 00 b9` | str w8,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bfaf88"></a> `00bfaf88` | `41 03 00 54` | b.ne 0x00bfaff0 | `CONDITIONAL_JUMP`
<a id="insn-00bfaf8c"></a> `00bfaf8c` | `88 22 40 f9` | ldr x8,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-00bfaf90"></a> `00bfaf90` | `c1 f6 7e d3` | lsl x1,x22,#0x2 | `FALL_THROUGH`
<a id="insn-00bfaf94"></a> `00bfaf94` | `80 1e 00 f9` | str x0,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00bfaf98"></a> `00bfaf98` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bfaf9c"></a> `00bfaf9c` | `41 7b 01 94` | bl 0x00c59ca0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfafa0"></a> `00bfafa0` | `c0 00 00 b5` | cbnz x0,0x00bfafb8 | `CONDITIONAL_JUMP`
<a id="insn-00bfafa4"></a> `00bfafa4` | `88 26 44 29` | ldp w8,w9,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bfafa8"></a> `00bfafa8` | `08 01 00 32` | orr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfafac"></a> `00bfafac` | `3f 01 08 6a` | tst w9,w8 | `FALL_THROUGH`
<a id="insn-00bfafb0"></a> `00bfafb0` | `88 22 00 b9` | str w8,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bfafb4"></a> `00bfafb4` | `e1 01 00 54` | b.ne 0x00bfaff0 | `CONDITIONAL_JUMP`
<a id="insn-00bfafb8"></a> `00bfafb8` | `89 26 40 f9` | ldr x9,[x20, #0x48] | `FALL_THROUGH`
<a id="insn-00bfafbc"></a> `00bfafbc` | `80 22 00 f9` | str x0,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-00bfafc0"></a> `00bfafc0` | `96 2a 00 f9` | str x22,[x20, #0x50] | `FALL_THROUGH`
<a id="insn-00bfafc4"></a> `00bfafc4` | `28 05 00 91` | add x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bfafc8"></a> `00bfafc8` | `8a 1e 40 f9` | ldr x10,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00bfafcc"></a> `00bfafcc` | `55 79 29 f8` | str x21,[x10, x9, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00bfafd0"></a> `00bfafd0` | `8a 22 40 f9` | ldr x10,[x20, #0x40] | `FALL_THROUGH`
<a id="insn-00bfafd4"></a> `00bfafd4` | `53 79 29 b8` | str w19,[x10, x9, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00bfafd8"></a> `00bfafd8` | `88 26 00 f9` | str x8,[x20, #0x48] | `FALL_THROUGH`
<a id="insn-00bfafdc"></a> `00bfafdc` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfafe0"></a> `00bfafe0` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfafe4"></a> `00bfafe4` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bfafe8"></a> `00bfafe8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfafec"></a> `00bfafec` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfaff0"></a> `00bfaff0` | `60 b5 ff b0` | adrp x0,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bfaff4"></a> `00bfaff4` | `00 68 11 91` | add x0,x0,#0x45a | `FALL_THROUGH`
<a id="insn-00bfaff8"></a> `00bfaff8` | `49 00 00 94` | bl 0x00bfb11c | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfaf1c`](#insn-00bfaf1c) 範囲 `[['00bfaf1c', '00bfaf4b']]`
  - `CONDITIONAL_JUMP` [`00bfaf48`](#insn-00bfaf48) → [`00bfafc8`](#insn-00bfafc8)
  - `FALL_THROUGH` [`00bfaf48`](#insn-00bfaf48) → [`00bfaf4c`](#insn-00bfaf4c)
- ブロック [`00bfaf4c`](#insn-00bfaf4c) 範囲 `[['00bfaf4c', '00bfaf77']]`
  - `CONDITIONAL_JUMP` [`00bfaf74`](#insn-00bfaf74) → [`00bfaf8c`](#insn-00bfaf8c)
  - `FALL_THROUGH` [`00bfaf74`](#insn-00bfaf74) → [`00bfaf78`](#insn-00bfaf78)
- ブロック [`00bfaf78`](#insn-00bfaf78) 範囲 `[['00bfaf78', '00bfaf8b']]`
  - `CONDITIONAL_JUMP` [`00bfaf88`](#insn-00bfaf88) → [`00bfaff0`](#insn-00bfaff0)
  - `FALL_THROUGH` [`00bfaf88`](#insn-00bfaf88) → [`00bfaf8c`](#insn-00bfaf8c)
- ブロック [`00bfaf8c`](#insn-00bfaf8c) 範囲 `[['00bfaf8c', '00bfafa3']]`
  - `CONDITIONAL_JUMP` [`00bfafa0`](#insn-00bfafa0) → [`00bfafb8`](#insn-00bfafb8)
  - `FALL_THROUGH` [`00bfafa0`](#insn-00bfafa0) → [`00bfafa4`](#insn-00bfafa4)
- ブロック [`00bfafa4`](#insn-00bfafa4) 範囲 `[['00bfafa4', '00bfafb7']]`
  - `CONDITIONAL_JUMP` [`00bfafb4`](#insn-00bfafb4) → [`00bfaff0`](#insn-00bfaff0)
  - `FALL_THROUGH` [`00bfafb4`](#insn-00bfafb4) → [`00bfafb8`](#insn-00bfafb8)
- ブロック [`00bfafb8`](#insn-00bfafb8) 範囲 `[['00bfafb8', '00bfafc7']]`
  - `FALL_THROUGH` [`00bfafc4`](#insn-00bfafc4) → [`00bfafc8`](#insn-00bfafc8)
- ブロック [`00bfafc8`](#insn-00bfafc8) 範囲 `[['00bfafc8', '00bfafef']]`
- ブロック [`00bfaff0`](#insn-00bfaff0) 範囲 `[['00bfaff0', '00bfaffb']]`

## 命令位置別の参照

- [`00bfaf20`](#insn-00bfaf20) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaf24`](#insn-00bfaf24) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaf28`](#insn-00bfaf28) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaf48`](#insn-00bfaf48) → [`00bfafc8`](#insn-00bfafc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaf70`](#insn-00bfaf70) → [`00c59ca0`](../00c59/00c59ca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59ca0` · 推定シンボル `None` · 推定型 `None`
- [`00bfaf74`](#insn-00bfaf74) → [`00bfaf8c`](#insn-00bfaf8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaf88`](#insn-00bfaf88) → [`00bfaff0`](#insn-00bfaff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaf9c`](#insn-00bfaf9c) → [`00c59ca0`](../00c59/00c59ca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59ca0` · 推定シンボル `None` · 推定型 `None`
- [`00bfafa0`](#insn-00bfafa0) → [`00bfafb8`](#insn-00bfafb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfafb4`](#insn-00bfafb4) → [`00bfaff0`](#insn-00bfaff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfafdc`](#insn-00bfafdc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfafe0`](#insn-00bfafe0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfafe4`](#insn-00bfafe4) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfaff4`](#insn-00bfaff4) → `002a745a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bfaff8`](#insn-00bfaff8) → [`00bfb11c`](../00bfb/00bfb11c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bfb11c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfaf20`](#insn-00bfaf20)

~~~json
{
  "source": "00bfaf20",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaf24`](#insn-00bfaf24)

~~~json
{
  "source": "00bfaf24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaf28`](#insn-00bfaf28)

~~~json
{
  "source": "00bfaf28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaf48`](#insn-00bfaf48)

~~~json
{
  "source": "00bfaf48",
  "target": "00bfafc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaf70`](#insn-00bfaf70)

~~~json
{
  "source": "00bfaf70",
  "target": "00c59ca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfaf74`](#insn-00bfaf74)

~~~json
{
  "source": "00bfaf74",
  "target": "00bfaf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaf88`](#insn-00bfaf88)

~~~json
{
  "source": "00bfaf88",
  "target": "00bfaff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaf9c`](#insn-00bfaf9c)

~~~json
{
  "source": "00bfaf9c",
  "target": "00c59ca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfafa0`](#insn-00bfafa0)

~~~json
{
  "source": "00bfafa0",
  "target": "00bfafb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfafb4`](#insn-00bfafb4)

~~~json
{
  "source": "00bfafb4",
  "target": "00bfaff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfafdc`](#insn-00bfafdc)

~~~json
{
  "source": "00bfafdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfafe0`](#insn-00bfafe0)

~~~json
{
  "source": "00bfafe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfafe4`](#insn-00bfafe4)

~~~json
{
  "source": "00bfafe4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfaff4`](#insn-00bfaff4)

~~~json
{
  "source": "00bfaff4",
  "target": "002a745a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a745a",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "696f735f626173653a3a636c65617200",
  "capture_start": "002a745a",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bfaff8`](#insn-00bfaff8)

~~~json
{
  "source": "00bfaff8",
  "target": "00bfb11c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
