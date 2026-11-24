# 00acbedc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00acbce0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbce0.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/detail_skipped-0005.md#compare-48b9bfc1a80400bebd8ff0a9d7c46994)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acbf4c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acbf4c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/detail_skipped-0006.md#compare-9db30ceb9584937b7df9a5242da60b2d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbedc",
  "name": "FUN_00acbedc",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "48fcdfe9a16c87dbb0c64eb9c2e9b8989f49cc6678ea6f79376522f7f9083028",
  "source_text_sha256": "48fcdfe9a16c87dbb0c64eb9c2e9b8989f49cc6678ea6f79376522f7f9083028",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acbedc",
        "00acbf17"
      ]
    ],
    "bytes_sha256": "7e7e1cda346a3bbb3103eba76ed8c923a01ef901c1edd08adfe9a5a12457a4fb",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0073202c](../00732/0073202c.md)
- [00935b10](../00935/00935b10.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 458 bytes

~~~c

int FUN_00acbedc(long param_1)

{
  long lVar1;
  int iVar2;
  long lVar3;
  
  if (*(long *)(param_1 + 0x30) == 0) {
    iVar2 = 0;
  }
  else {
    iVar2 = 0;
    lVar1 = *(long *)(param_1 + 0x30);
    lVar3 = param_1;
    do {
      param_1 = lVar1;
      iVar2 = *(int *)(lVar3 + 0xc) + iVar2;
      lVar1 = *(long *)(param_1 + 0x30);
      lVar3 = param_1;
    } while (*(long *)(param_1 + 0x30) != 0);
  }
  return *(int *)(param_1 + 0xc) + iVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acbedc"></a> `00acbedc` | `09 18 40 f9` | ldr x9,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00acbee0"></a> `00acbee0` | `49 01 00 b4` | cbz x9,0x00acbf08 | `CONDITIONAL_JUMP`
<a id="insn-00acbee4"></a> `00acbee4` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00acbee8"></a> `00acbee8` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00acbeec"></a> `00acbeec` | `4a 0d 40 b9` | ldr w10,[x10, #0xc] | `FALL_THROUGH`
<a id="insn-00acbef0"></a> `00acbef0` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-00acbef4"></a> `00acbef4` | `29 19 40 f9` | ldr x9,[x9, #0x30] | `FALL_THROUGH`
<a id="insn-00acbef8"></a> `00acbef8` | `48 01 08 0b` | add w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00acbefc"></a> `00acbefc` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00acbf00"></a> `00acbf00` | `69 ff ff b5` | cbnz x9,0x00acbeec | `CONDITIONAL_JUMP`
<a id="insn-00acbf04"></a> `00acbf04` | `02 00 00 14` | b 0x00acbf0c | `UNCONDITIONAL_JUMP`
<a id="insn-00acbf08"></a> `00acbf08` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00acbf0c"></a> `00acbf0c` | `09 0c 40 b9` | ldr w9,[x0, #0xc] | `FALL_THROUGH`
<a id="insn-00acbf10"></a> `00acbf10` | `20 01 08 0b` | add w0,w9,w8 | `FALL_THROUGH`
<a id="insn-00acbf14"></a> `00acbf14` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acbedc`](#insn-00acbedc) 範囲 `[['00acbedc', '00acbee3']]`
  - `CONDITIONAL_JUMP` [`00acbee0`](#insn-00acbee0) → [`00acbf08`](#insn-00acbf08)
  - `FALL_THROUGH` [`00acbee0`](#insn-00acbee0) → [`00acbee4`](#insn-00acbee4)
- ブロック [`00acbee4`](#insn-00acbee4) 範囲 `[['00acbee4', '00acbeeb']]`
  - `FALL_THROUGH` [`00acbee8`](#insn-00acbee8) → [`00acbeec`](#insn-00acbeec)
- ブロック [`00acbeec`](#insn-00acbeec) 範囲 `[['00acbeec', '00acbf03']]`
  - `CONDITIONAL_JUMP` [`00acbf00`](#insn-00acbf00) → [`00acbeec`](#insn-00acbeec)
  - `FALL_THROUGH` [`00acbf00`](#insn-00acbf00) → [`00acbf04`](#insn-00acbf04)
- ブロック [`00acbf04`](#insn-00acbf04) 範囲 `[['00acbf04', '00acbf07']]`
  - `UNCONDITIONAL_JUMP` [`00acbf04`](#insn-00acbf04) → [`00acbf0c`](#insn-00acbf0c)
- ブロック [`00acbf08`](#insn-00acbf08) 範囲 `[['00acbf08', '00acbf0b']]`
  - `FALL_THROUGH` [`00acbf08`](#insn-00acbf08) → [`00acbf0c`](#insn-00acbf0c)
- ブロック [`00acbf0c`](#insn-00acbf0c) 範囲 `[['00acbf0c', '00acbf17']]`

## 命令位置別の参照

- [`00acbee0`](#insn-00acbee0) → [`00acbf08`](#insn-00acbf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf00`](#insn-00acbf00) → [`00acbeec`](#insn-00acbeec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf04`](#insn-00acbf04) → [`00acbf0c`](#insn-00acbf0c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbee0`](#insn-00acbee0)

~~~json
{
  "source": "00acbee0",
  "target": "00acbf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf00`](#insn-00acbf00)

~~~json
{
  "source": "00acbf00",
  "target": "00acbeec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf04`](#insn-00acbf04)

~~~json
{
  "source": "00acbf04",
  "target": "00acbf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
