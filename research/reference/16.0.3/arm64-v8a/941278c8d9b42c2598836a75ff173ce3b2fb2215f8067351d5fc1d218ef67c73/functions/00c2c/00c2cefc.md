# 00c2cefc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c2bf08`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2b/00c2bf08.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0089.md#compare-9127fe6ed6692e272cf65ca82d7c5b47)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c2cefc",
  "name": "_ZNSt6__ndk18numpunctIcEC2Em",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "587f2c0bf98683396df8bbf0ee4d6722768cabdf3f2b3aa22a8bfd6647efa85b",
  "source_text_sha256": "587f2c0bf98683396df8bbf0ee4d6722768cabdf3f2b3aa22a8bfd6647efa85b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c2cefc",
        "00c2cf27"
      ]
    ],
    "bytes_sha256": "c70962a741ac534823dd80256096bb6b05846c715dd2731d41d763070dcb3fc6",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5f8a0](../00c5f/00c5f8a0.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 316 bytes

~~~c

void _ZNSt6__ndk18numpunctIcEC2Em(long *param_1,long param_2)

{
  undefined *puVar1;
  
  puVar1 = PTR__ZTVNSt6__ndk18numpunctIcEE_00c9ce88;
  *(undefined2 *)(param_1 + 2) = 0x2c2e;
  param_1[4] = 0;
  param_1[5] = 0;
  param_1[3] = 0;
  *param_1 = (long)(puVar1 + 0x10);
  param_1[1] = param_2 + -1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c2cefc"></a> `00c2cefc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00c2cf00"></a> `00c2cf00` | `89 03 00 90` | adrp x9,0xc9c000 | `FALL_THROUGH`
<a id="insn-00c2cf04"></a> `00c2cf04` | `c8 85 85 52` | mov w8,#0x2c2e | `FALL_THROUGH`
<a id="insn-00c2cf08"></a> `00c2cf08` | `29 45 47 f9` | ldr x9,[x9, #0xe88] | `FALL_THROUGH`
<a id="insn-00c2cf0c"></a> `00c2cf0c` | `08 20 00 79` | strh w8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00c2cf10"></a> `00c2cf10` | `28 04 00 d1` | sub x8,x1,#0x1 | `FALL_THROUGH`
<a id="insn-00c2cf14"></a> `00c2cf14` | `1f 7c 02 a9` | stp xzr,xzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00c2cf18"></a> `00c2cf18` | `29 41 00 91` | add x9,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00c2cf1c"></a> `00c2cf1c` | `1f 0c 00 f9` | str xzr,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00c2cf20"></a> `00c2cf20` | `09 20 00 a9` | stp x9,x8,[x0] | `FALL_THROUGH`
<a id="insn-00c2cf24"></a> `00c2cf24` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c2cefc`](#insn-00c2cefc) 範囲 `[['00c2cefc', '00c2cf27']]`

## 命令位置別の参照

- [`00c2cf08`](#insn-00c2cf08) → `00c9ce88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c2cf20`](#insn-00c2cf20) → `00c949c0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c2cf08`](#insn-00c2cf08)

~~~json
{
  "source": "00c2cf08",
  "target": "00c9ce88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ce88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c2cf20`](#insn-00c2cf20)

~~~json
{
  "source": "00c2cf20",
  "target": "00c949c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c949b0",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
