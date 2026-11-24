# 00bdda0c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdd970`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd970.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-e1d060a322373a114240506ea8ab0f75)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bdea00`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdea00.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-1eb13c5f1aebaa5470c309419f5a281d)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdda0c",
  "name": "_ZN8firebase4auth8metadata12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9c904d7893f87d924a980a84bed0833f62ebb4284a89c6f55fe091bbae9f000e",
  "source_text_sha256": "9c904d7893f87d924a980a84bed0833f62ebb4284a89c6f55fe091bbae9f000e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdda0c",
        "00bdda7b"
      ]
    ],
    "bytes_sha256": "d3ab5952162d269b89cd9aa229a04db5b3c1e37ab74d8dcc6fb7bde62331a1ea",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b030](../00c5b/00c5b030.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 382 bytes

~~~c

void _ZN8firebase4auth8metadata12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_01126f00 != 0) {
    if (DAT_01126f08 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126f08 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126f00);
    DAT_01126f00 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdda0c"></a> `00bdda0c` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bdda10"></a> `00bdda10` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdda14"></a> `00bdda14` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdda18"></a> `00bdda18` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdda1c"></a> `00bdda1c` | `54 2a 00 b0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdda20"></a> `00bdda20` | `81 82 47 f9` | ldr x1,[x20, #0xf00] | `FALL_THROUGH`
<a id="insn-00bdda24"></a> `00bdda24` | `41 02 00 b4` | cbz x1,0x00bdda6c | `CONDITIONAL_JUMP`
<a id="insn-00bdda28"></a> `00bdda28` | `55 2a 00 b0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdda2c"></a> `00bdda2c` | `a8 22 7c 39` | ldrb w8,[x21, #0xf08] | `FALL_THROUGH`
<a id="insn-00bdda30"></a> `00bdda30` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdda34"></a> `00bdda34` | `c8 00 00 34` | cbz w8,0x00bdda4c | `CONDITIONAL_JUMP`
<a id="insn-00bdda38"></a> `00bdda38` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdda3c"></a> `00bdda3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdda40"></a> `00bdda40` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bdda44"></a> `00bdda44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdda48"></a> `00bdda48` | `bf 22 3c 39` | strb wzr,[x21, #0xf08] | `FALL_THROUGH`
<a id="insn-00bdda4c"></a> `00bdda4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdda50"></a> `00bdda50` | `78 f5 01 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bdda54"></a> `00bdda54` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdda58"></a> `00bdda58` | `81 82 47 f9` | ldr x1,[x20, #0xf00] | `FALL_THROUGH`
<a id="insn-00bdda5c"></a> `00bdda5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdda60"></a> `00bdda60` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bdda64"></a> `00bdda64` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdda68"></a> `00bdda68` | `9f 82 07 f9` | str xzr,[x20, #0xf00] | `FALL_THROUGH`
<a id="insn-00bdda6c"></a> `00bdda6c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdda70"></a> `00bdda70` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdda74"></a> `00bdda74` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bdda78"></a> `00bdda78` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdda0c`](#insn-00bdda0c) 範囲 `[['00bdda0c', '00bdda27']]`
  - `CONDITIONAL_JUMP` [`00bdda24`](#insn-00bdda24) → [`00bdda6c`](#insn-00bdda6c)
  - `FALL_THROUGH` [`00bdda24`](#insn-00bdda24) → [`00bdda28`](#insn-00bdda28)
- ブロック [`00bdda28`](#insn-00bdda28) 範囲 `[['00bdda28', '00bdda37']]`
  - `CONDITIONAL_JUMP` [`00bdda34`](#insn-00bdda34) → [`00bdda4c`](#insn-00bdda4c)
  - `FALL_THROUGH` [`00bdda34`](#insn-00bdda34) → [`00bdda38`](#insn-00bdda38)
- ブロック [`00bdda38`](#insn-00bdda38) 範囲 `[['00bdda38', '00bdda4b']]`
  - `FALL_THROUGH` [`00bdda48`](#insn-00bdda48) → [`00bdda4c`](#insn-00bdda4c)
- ブロック [`00bdda4c`](#insn-00bdda4c) 範囲 `[['00bdda4c', '00bdda6b']]`
  - `FALL_THROUGH` [`00bdda68`](#insn-00bdda68) → [`00bdda6c`](#insn-00bdda6c)
- ブロック [`00bdda6c`](#insn-00bdda6c) 範囲 `[['00bdda6c', '00bdda7b']]`

## 命令位置別の参照

- [`00bdda0c`](#insn-00bdda0c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdda10`](#insn-00bdda10) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdda14`](#insn-00bdda14) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdda20`](#insn-00bdda20) → `01126f00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdda24`](#insn-00bdda24) → [`00bdda6c`](#insn-00bdda6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdda2c`](#insn-00bdda2c) → `01126f08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdda34`](#insn-00bdda34) → [`00bdda4c`](#insn-00bdda4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdda48`](#insn-00bdda48) → `01126f08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdda50`](#insn-00bdda50) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bdda58`](#insn-00bdda58) → `01126f00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdda68`](#insn-00bdda68) → `01126f00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdda6c`](#insn-00bdda6c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdda70`](#insn-00bdda70) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdda0c`](#insn-00bdda0c)

~~~json
{
  "source": "00bdda0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdda10`](#insn-00bdda10)

~~~json
{
  "source": "00bdda10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdda14`](#insn-00bdda14)

~~~json
{
  "source": "00bdda14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdda20`](#insn-00bdda20)

~~~json
{
  "source": "00bdda20",
  "target": "01126f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdda24`](#insn-00bdda24)

~~~json
{
  "source": "00bdda24",
  "target": "00bdda6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdda2c`](#insn-00bdda2c)

~~~json
{
  "source": "00bdda2c",
  "target": "01126f08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f08",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdda34`](#insn-00bdda34)

~~~json
{
  "source": "00bdda34",
  "target": "00bdda4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdda48`](#insn-00bdda48)

~~~json
{
  "source": "00bdda48",
  "target": "01126f08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f08",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdda50`](#insn-00bdda50)

~~~json
{
  "source": "00bdda50",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdda58`](#insn-00bdda58)

~~~json
{
  "source": "00bdda58",
  "target": "01126f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdda68`](#insn-00bdda68)

~~~json
{
  "source": "00bdda68",
  "target": "01126f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdda6c`](#insn-00bdda6c)

~~~json
{
  "source": "00bdda6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdda70`](#insn-00bdda70)

~~~json
{
  "source": "00bdda70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
