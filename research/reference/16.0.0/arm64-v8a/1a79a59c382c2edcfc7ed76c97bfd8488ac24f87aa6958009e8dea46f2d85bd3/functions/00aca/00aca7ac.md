# 00aca7ac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0162.md#review-9b9aa0281641b64f408890c9c0cf0ed2)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aca9a8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00aca9a8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-2a15719169d82b6f3a1e0d4e118cb1a1)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aca7ac",
  "name": "FUN_00aca7ac",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "46534f1daf495d0918287df2e50222c127c7c4529608418f7ae9625c2fffa27b",
  "source_text_sha256": "46534f1daf495d0918287df2e50222c127c7c4529608418f7ae9625c2fffa27b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aca7ac",
        "00aca83b"
      ]
    ],
    "bytes_sha256": "0810872d7d55ecc789cecb09c23b3f29cc74188209892ae90b05f3d70b94dce4",
    "instruction_count": 36,
    "instruction_bytes": 144,
    "body_bytes": 144,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00789da0](../00789/00789da0.md)
- [0082fb2c](../0082f/0082fb2c.md)
- [008feea4](../008fe/008feea4.md)
- [00a3e32c](../00a3e/00a3e32c.md)
- [00ac08a0](../00ac0/00ac08a0.md)

## 呼び出し先

- [00467820](../00467/00467820.md)
- [00467aec](../00467/00467aec.md)
- [00467f14](../00467/00467f14.md)
- [0046c984](../0046c/0046c984.md)
- [0046ca44](../0046c/0046ca44.md)
- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 534 bytes

~~~c

void FUN_00aca7ac(long param_1)

{
  int iVar1;
  undefined4 uVar2;
  undefined4 uVar3;
  undefined8 uVar4;
  long lVar5;
  
  if (*(char *)(param_1 + 0x94) != '\0') {
    uVar4 = FUN_00467820();
    FUN_00467aec(uVar4,0,0,0,*(int *)(param_1 + 0x90) * 0x14);
    lVar5 = FUN_008514b8();
    iVar1 = *(int *)((long)&fde_table_entry_003339e8.initial_loc + lVar5);
    FUN_008514b8();
    uVar2 = FUN_0046c984();
    FUN_008514b8();
    uVar3 = FUN_0046ca44();
    FUN_00467f14(uVar4,0,-iVar1,uVar2,uVar3);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aca7ac"></a> `00aca7ac` | `08 50 42 39` | ldrb w8,[x0, #0x94] | `FALL_THROUGH`
<a id="insn-00aca7b0"></a> `00aca7b0` | `48 04 00 34` | cbz w8,0x00aca838 | `CONDITIONAL_JUMP`
<a id="insn-00aca7b4"></a> `00aca7b4` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aca7b8"></a> `00aca7b8` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aca7bc"></a> `00aca7bc` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aca7c0"></a> `00aca7c0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aca7c4"></a> `00aca7c4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aca7c8"></a> `00aca7c8` | `16 74 e6 97` | bl 0x00467820 | `UNCONDITIONAL_CALL`
<a id="insn-00aca7cc"></a> `00aca7cc` | `68 92 40 b9` | ldr w8,[x19, #0x90] | `FALL_THROUGH`
<a id="insn-00aca7d0"></a> `00aca7d0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aca7d4"></a> `00aca7d4` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aca7d8"></a> `00aca7d8` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00aca7dc"></a> `00aca7dc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aca7e0"></a> `00aca7e0` | `08 09 08 0b` | add w8,w8,w8, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00aca7e4"></a> `00aca7e4` | `04 75 1e 53` | lsl w4,w8,#0x2 | `FALL_THROUGH`
<a id="insn-00aca7e8"></a> `00aca7e8` | `c1 74 e6 97` | bl 0x00467aec | `UNCONDITIONAL_CALL`
<a id="insn-00aca7ec"></a> `00aca7ec` | `33 1b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aca7f0"></a> `00aca7f0` | `08 3d 87 52` | mov w8,#0x39e8 | `FALL_THROUGH`
<a id="insn-00aca7f4"></a> `00aca7f4` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00aca7f8"></a> `00aca7f8` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aca7fc"></a> `00aca7fc` | `f4 03 08 4b` | neg w20,w8 | `FALL_THROUGH`
<a id="insn-00aca800"></a> `00aca800` | `2e 1b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aca804"></a> `00aca804` | `60 88 e6 97` | bl 0x0046c984 | `UNCONDITIONAL_CALL`
<a id="insn-00aca808"></a> `00aca808` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aca80c"></a> `00aca80c` | `2b 1b f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aca810"></a> `00aca810` | `8d 88 e6 97` | bl 0x0046ca44 | `UNCONDITIONAL_CALL`
<a id="insn-00aca814"></a> `00aca814` | `e4 03 00 2a` | mov w4,w0 | `FALL_THROUGH`
<a id="insn-00aca818"></a> `00aca818` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aca81c"></a> `00aca81c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aca820"></a> `00aca820` | `e2 03 14 2a` | mov w2,w20 | `FALL_THROUGH`
<a id="insn-00aca824"></a> `00aca824` | `e3 03 15 2a` | mov w3,w21 | `FALL_THROUGH`
<a id="insn-00aca828"></a> `00aca828` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aca82c"></a> `00aca82c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aca830"></a> `00aca830` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aca834"></a> `00aca834` | `b8 75 e6 17` | b 0x00467f14 | `CALL_TERMINATOR`
<a id="insn-00aca838"></a> `00aca838` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aca7ac`](#insn-00aca7ac) 範囲 `[['00aca7ac', '00aca7b3']]`
  - `CONDITIONAL_JUMP` [`00aca7b0`](#insn-00aca7b0) → [`00aca838`](#insn-00aca838)
  - `FALL_THROUGH` [`00aca7b0`](#insn-00aca7b0) → [`00aca7b4`](#insn-00aca7b4)
- ブロック [`00aca7b4`](#insn-00aca7b4) 範囲 `[['00aca7b4', '00aca837']]`
- ブロック [`00aca838`](#insn-00aca838) 範囲 `[['00aca838', '00aca83b']]`

## 命令位置別の参照

- [`00aca7b0`](#insn-00aca7b0) → [`00aca838`](#insn-00aca838) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca7b4`](#insn-00aca7b4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca7b8`](#insn-00aca7b8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca7bc`](#insn-00aca7bc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca7c8`](#insn-00aca7c8) → [`00467820`](../00467/00467820.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467820` · 推定シンボル `None` · 推定型 `None`
- [`00aca7e8`](#insn-00aca7e8) → [`00467aec`](../00467/00467aec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467aec` · 推定シンボル `None` · 推定型 `None`
- [`00aca7ec`](#insn-00aca7ec) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00aca7f8`](#insn-00aca7f8) → `003339e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00aca800`](#insn-00aca800) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00aca804`](#insn-00aca804) → [`0046c984`](../0046c/0046c984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c984` · 推定シンボル `None` · 推定型 `None`
- [`00aca80c`](#insn-00aca80c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00aca810`](#insn-00aca810) → [`0046ca44`](../0046c/0046ca44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca44` · 推定シンボル `None` · 推定型 `None`
- [`00aca828`](#insn-00aca828) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca82c`](#insn-00aca82c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca830`](#insn-00aca830) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca834`](#insn-00aca834) → [`00467f14`](../00467/00467f14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467f14` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aca7b0`](#insn-00aca7b0)

~~~json
{
  "source": "00aca7b0",
  "target": "00aca838",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca7b4`](#insn-00aca7b4)

~~~json
{
  "source": "00aca7b4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca7b8`](#insn-00aca7b8)

~~~json
{
  "source": "00aca7b8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca7bc`](#insn-00aca7bc)

~~~json
{
  "source": "00aca7bc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca7c8`](#insn-00aca7c8)

~~~json
{
  "source": "00aca7c8",
  "target": "00467820",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca7e8`](#insn-00aca7e8)

~~~json
{
  "source": "00aca7e8",
  "target": "00467aec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca7ec`](#insn-00aca7ec)

~~~json
{
  "source": "00aca7ec",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca7f8`](#insn-00aca7f8)

~~~json
{
  "source": "00aca7f8",
  "target": "003339e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003339e8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "44c26a00bc790900",
  "capture_start": "003339e8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aca800`](#insn-00aca800)

~~~json
{
  "source": "00aca800",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca804`](#insn-00aca804)

~~~json
{
  "source": "00aca804",
  "target": "0046c984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca80c`](#insn-00aca80c)

~~~json
{
  "source": "00aca80c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca810`](#insn-00aca810)

~~~json
{
  "source": "00aca810",
  "target": "0046ca44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aca828`](#insn-00aca828)

~~~json
{
  "source": "00aca828",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca82c`](#insn-00aca82c)

~~~json
{
  "source": "00aca82c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca830`](#insn-00aca830)

~~~json
{
  "source": "00aca830",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca834`](#insn-00aca834)

~~~json
{
  "source": "00aca834",
  "target": "00467f14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
