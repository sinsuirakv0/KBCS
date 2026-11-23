# 009daccc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `009daccc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009da/009daccc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/machine_only_observed-0038.md#compare-438c382cecf40c4367169f3d89a5e87e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009daccc",
  "name": "FUN_009daccc",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "05852a046441cc871d216dec7aee2490b4e5dd1875f36af17ed75096b9ff6c78",
  "source_text_sha256": "05852a046441cc871d216dec7aee2490b4e5dd1875f36af17ed75096b9ff6c78",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009daccc",
        "009dad5b"
      ],
      [
        "009dad98",
        "009dad9b"
      ]
    ],
    "bytes_sha256": "5e73db22a4abd99c1c6ad43382b1d969afd6a3c7234bbe6937030cfc3addf71e",
    "instruction_count": 37,
    "instruction_bytes": 148,
    "body_bytes": 148,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0060b7bc](../0060b/0060b7bc.md)
- [007317b0](../00731/007317b0.md)

## 呼び出し先

- [0053f81c](../0053f/0053f81c.md)
- [009daa10](../009da/009daa10.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 674 bytes

~~~c

void FUN_009daccc(undefined8 param_1)

{
  long lVar1;
  byte local_58 [16];
  void *local_48;
  byte local_40 [16];
  void *local_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  FUN_009daa10(local_40);
  local_58[5] = 0;
  local_58[0] = 8;
  local_58[1] = 0x3c;
  local_58[2] = 0x62;
  local_58[3] = 0x72;
  local_58[4] = 0x3e;
  FUN_0053f81c(param_1,local_40,local_58);
  if ((local_58[0] & 1) != 0) {
    _ZdlPv(local_48);
  }
  if ((local_40[0] & 1) != 0) {
    _ZdlPv(local_30);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
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
<a id="insn-009daccc"></a> `009daccc` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-009dacd0"></a> `009dacd0` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009dacd4"></a> `009dacd4` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009dacd8"></a> `009dacd8` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-009dacdc"></a> `009dacdc` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-009dace0"></a> `009dace0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-009dace4"></a> `009dace4` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-009dace8"></a> `009dace8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009dacec"></a> `009dacec` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009dacf0"></a> `009dacf0` | `48 ff ff 97` | bl 0x009daa10 | `UNCONDITIONAL_CALL`
<a id="insn-009dacf4"></a> `009dacf4` | `89 47 8c 52` | mov w9,#0x623c | `FALL_THROUGH`
<a id="insn-009dacf8"></a> `009dacf8` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-009dacfc"></a> `009dacfc` | `ff 37 00 39` | strb wzr,[sp, #0xd] | `FALL_THROUGH`
<a id="insn-009dad00"></a> `009dad00` | `49 ce a7 72` | movk w9,#0x3e72, LSL #16 | `FALL_THROUGH`
<a id="insn-009dad04"></a> `009dad04` | `e8 23 00 39` | strb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009dad08"></a> `009dad08` | `e9 93 00 b8` | stur w9,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-009dad0c"></a> `009dad0c` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009dad10"></a> `009dad10` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-009dad14"></a> `009dad14` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-009dad18"></a> `009dad18` | `c1 92 ed 97` | bl 0x0053f81c | `UNCONDITIONAL_CALL`
<a id="insn-009dad1c"></a> `009dad1c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009dad20"></a> `009dad20` | `68 00 00 36` | tbz w8,#0x0,0x009dad2c | `CONDITIONAL_JUMP`
<a id="insn-009dad24"></a> `009dad24` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009dad28"></a> `009dad28` | `8e 00 08 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-009dad2c"></a> `009dad2c` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009dad30"></a> `009dad30` | `68 00 00 36` | tbz w8,#0x0,0x009dad3c | `CONDITIONAL_JUMP`
<a id="insn-009dad34"></a> `009dad34` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009dad38"></a> `009dad38` | `8a 00 08 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-009dad3c"></a> `009dad3c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-009dad40"></a> `009dad40` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009dad44"></a> `009dad44` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009dad48"></a> `009dad48` | `81 02 00 54` | b.ne 0x009dad98 | `CONDITIONAL_JUMP`
<a id="insn-009dad4c"></a> `009dad4c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009dad50"></a> `009dad50` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009dad54"></a> `009dad54` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-009dad58"></a> `009dad58` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009dad98"></a> `009dad98` | `7e 00 08 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009daccc`](#insn-009daccc) 範囲 `[['009daccc', '009dad23']]`
  - `CONDITIONAL_JUMP` [`009dad20`](#insn-009dad20) → [`009dad2c`](#insn-009dad2c)
  - `FALL_THROUGH` [`009dad20`](#insn-009dad20) → [`009dad24`](#insn-009dad24)
- ブロック [`009dad24`](#insn-009dad24) 範囲 `[['009dad24', '009dad2b']]`
  - `FALL_THROUGH` [`009dad28`](#insn-009dad28) → [`009dad2c`](#insn-009dad2c)
- ブロック [`009dad2c`](#insn-009dad2c) 範囲 `[['009dad2c', '009dad33']]`
  - `CONDITIONAL_JUMP` [`009dad30`](#insn-009dad30) → [`009dad3c`](#insn-009dad3c)
  - `FALL_THROUGH` [`009dad30`](#insn-009dad30) → [`009dad34`](#insn-009dad34)
- ブロック [`009dad34`](#insn-009dad34) 範囲 `[['009dad34', '009dad3b']]`
  - `FALL_THROUGH` [`009dad38`](#insn-009dad38) → [`009dad3c`](#insn-009dad3c)
- ブロック [`009dad3c`](#insn-009dad3c) 範囲 `[['009dad3c', '009dad4b']]`
  - `CONDITIONAL_JUMP` [`009dad48`](#insn-009dad48) → [`009dad98`](#insn-009dad98)
  - `FALL_THROUGH` [`009dad48`](#insn-009dad48) → [`009dad4c`](#insn-009dad4c)
- ブロック [`009dad4c`](#insn-009dad4c) 範囲 `[['009dad4c', '009dad5b']]`
- ブロック [`009dad98`](#insn-009dad98) 範囲 `[['009dad98', '009dad9b']]`

## 命令位置別の参照

- [`009dacd0`](#insn-009dacd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dacd4`](#insn-009dacd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dace8`](#insn-009dace8) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dacf0`](#insn-009dacf0) → [`009daa10`](009daa10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009daa10` · 推定シンボル `None` · 推定型 `None`
- [`009dacfc`](#insn-009dacfc) → `Stack[-0x53]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dad04`](#insn-009dad04) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dad08`](#insn-009dad08) → `Stack[-0x57]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dad18`](#insn-009dad18) → [`0053f81c`](../0053f/0053f81c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0053f81c` · 推定シンボル `None` · 推定型 `None`
- [`009dad1c`](#insn-009dad1c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dad20`](#insn-009dad20) → [`009dad2c`](#insn-009dad2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dad24`](#insn-009dad24) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dad28`](#insn-009dad28) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`009dad2c`](#insn-009dad2c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dad30`](#insn-009dad30) → [`009dad3c`](#insn-009dad3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dad34`](#insn-009dad34) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dad38`](#insn-009dad38) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`009dad40`](#insn-009dad40) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dad48`](#insn-009dad48) → [`009dad98`](#insn-009dad98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dad4c`](#insn-009dad4c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dad50`](#insn-009dad50) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009dad98`](#insn-009dad98) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009dacd0`](#insn-009dacd0)

~~~json
{
  "source": "009dacd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dacd4`](#insn-009dacd4)

~~~json
{
  "source": "009dacd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dace8`](#insn-009dace8)

~~~json
{
  "source": "009dace8",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dacf0`](#insn-009dacf0)

~~~json
{
  "source": "009dacf0",
  "target": "009daa10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009dacfc`](#insn-009dacfc)

~~~json
{
  "source": "009dacfc",
  "target": "Stack[-0x53]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dad04`](#insn-009dad04)

~~~json
{
  "source": "009dad04",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dad08`](#insn-009dad08)

~~~json
{
  "source": "009dad08",
  "target": "Stack[-0x57]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dad18`](#insn-009dad18)

~~~json
{
  "source": "009dad18",
  "target": "0053f81c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009dad1c`](#insn-009dad1c)

~~~json
{
  "source": "009dad1c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dad20`](#insn-009dad20)

~~~json
{
  "source": "009dad20",
  "target": "009dad2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dad24`](#insn-009dad24)

~~~json
{
  "source": "009dad24",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dad28`](#insn-009dad28)

~~~json
{
  "source": "009dad28",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009dad2c`](#insn-009dad2c)

~~~json
{
  "source": "009dad2c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dad30`](#insn-009dad30)

~~~json
{
  "source": "009dad30",
  "target": "009dad3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dad34`](#insn-009dad34)

~~~json
{
  "source": "009dad34",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dad38`](#insn-009dad38)

~~~json
{
  "source": "009dad38",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009dad40`](#insn-009dad40)

~~~json
{
  "source": "009dad40",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dad48`](#insn-009dad48)

~~~json
{
  "source": "009dad48",
  "target": "009dad98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dad4c`](#insn-009dad4c)

~~~json
{
  "source": "009dad4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dad50`](#insn-009dad50)

~~~json
{
  "source": "009dad50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009dad98`](#insn-009dad98)

~~~json
{
  "source": "009dad98",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
