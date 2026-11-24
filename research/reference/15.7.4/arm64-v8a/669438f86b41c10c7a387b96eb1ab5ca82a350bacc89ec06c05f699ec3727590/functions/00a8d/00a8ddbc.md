# 00a8ddbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a8dd78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8dd78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0002.md#compare-f478043390580153b05f5749bf20c9c4)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0080.md#review-382f44bb7e20c2f1af2be309c8061d8f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a8ddbc",
  "name": "FUN_00a8ddbc",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c41cda0609d65a0dda0b241186977d50c8f6c7408f00be59ec28d55e3f437177",
  "source_text_sha256": "c41cda0609d65a0dda0b241186977d50c8f6c7408f00be59ec28d55e3f437177",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a8ddbc",
        "00a8ddfb"
      ]
    ],
    "bytes_sha256": "530138e8b909e7fa071bbee47bc1b081e9107439764f56d86a7b4685e89ecd04",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 392 bytes

~~~c

void FUN_00a8ddbc(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  
  puVar1 = (undefined8 *)_Znwm(0x20);
  uVar4 = *(undefined8 *)(param_1 + 0x10);
  uVar3 = *(undefined8 *)(param_1 + 8);
  uVar2 = *(undefined8 *)(param_1 + 0x18);
  *puVar1 = &PTR_FUN_00c0e0d8;
  puVar1[2] = uVar4;
  puVar1[1] = uVar3;
  puVar1[3] = uVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a8ddbc"></a> `00a8ddbc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00a8ddc0"></a> `00a8ddc0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a8ddc4"></a> `00a8ddc4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a8ddc8"></a> `00a8ddc8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a8ddcc"></a> `00a8ddcc` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00a8ddd0"></a> `00a8ddd0` | `9c 34 05 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00a8ddd4"></a> `00a8ddd4` | `60 82 c0 3c` | ldur q0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00a8ddd8"></a> `00a8ddd8` | `69 0e 40 f9` | ldr x9,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00a8dddc"></a> `00a8dddc` | `08 0c 00 b0` | adrp x8,0xc0e000 | `FALL_THROUGH`
<a id="insn-00a8dde0"></a> `00a8dde0` | `08 61 03 91` | add x8,x8,#0xd8 | `FALL_THROUGH`
<a id="insn-00a8dde4"></a> `00a8dde4` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00a8dde8"></a> `00a8dde8` | `00 80 80 3c` | stur q0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00a8ddec"></a> `00a8ddec` | `09 0c 00 f9` | str x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00a8ddf0"></a> `00a8ddf0` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a8ddf4"></a> `00a8ddf4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00a8ddf8"></a> `00a8ddf8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a8ddbc`](#insn-00a8ddbc) 範囲 `[['00a8ddbc', '00a8ddfb']]`

## 命令位置別の参照

- [`00a8ddbc`](#insn-00a8ddbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8ddc0`](#insn-00a8ddc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8ddd0`](#insn-00a8ddd0) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00a8dde4`](#insn-00a8dde4) → `00c0e0d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00a8ddf0`](#insn-00a8ddf0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8ddf4`](#insn-00a8ddf4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a8ddbc`](#insn-00a8ddbc)

~~~json
{
  "source": "00a8ddbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8ddc0`](#insn-00a8ddc0)

~~~json
{
  "source": "00a8ddc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8ddd0`](#insn-00a8ddd0)

~~~json
{
  "source": "00a8ddd0",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8dde4`](#insn-00a8dde4)

~~~json
{
  "source": "00a8dde4",
  "target": "00c0e0d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0e0d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a8ddf0`](#insn-00a8ddf0)

~~~json
{
  "source": "00a8ddf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8ddf4`](#insn-00a8ddf4)

~~~json
{
  "source": "00a8ddf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
