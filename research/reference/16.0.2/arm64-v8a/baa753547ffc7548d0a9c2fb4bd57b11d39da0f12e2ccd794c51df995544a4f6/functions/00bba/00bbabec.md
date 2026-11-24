# 00bbabec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbab50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bba/00bbab50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0079.md#compare-73e20f37f23fe134e136aec305f7b2e4)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bbbbe0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbbe0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0079.md#compare-9c22a72484e44f97abcc0ce7753fc957)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbabec",
  "name": "FUN_00bbabec",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "92b7b5b26eab11bca475cffb74b0e274b80c3f388c89970a67b50e528d41b108",
  "source_text_sha256": "92b7b5b26eab11bca475cffb74b0e274b80c3f388c89970a67b50e528d41b108",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbabec",
        "00bbaca7"
      ]
    ],
    "bytes_sha256": "97ff43bb8bd6b4e924bf78894103c29be8eafc83bf95e4edab33e3cf92f23ac2",
    "instruction_count": 47,
    "instruction_bytes": 188,
    "body_bytes": 188,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

- [00bba6c4](../00bba/00bba6c4.md)
- [00bbb0f4](../00bbb/00bbb0f4.md)

## 呼び出し先

- [00c5b030](../00c5b/00c5b030.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 638 bytes

~~~c

void FUN_00bbabec(long *param_1)

{
  if (DAT_011263a8 != 0) {
    if (DAT_011263b0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011263b0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011263a8);
    DAT_011263a8 = 0;
  }
  if (DAT_01126418 != 0) {
    if (DAT_01126420 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126420 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126418);
    DAT_01126418 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbabec"></a> `00bbabec` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bbabf0"></a> `00bbabf0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbabf4"></a> `00bbabf4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbabf8"></a> `00bbabf8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbabfc"></a> `00bbabfc` | `74 2b 00 90` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbac00"></a> `00bbac00` | `81 d6 41 f9` | ldr x1,[x20, #0x3a8] | `FALL_THROUGH`
<a id="insn-00bbac04"></a> `00bbac04` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbac08"></a> `00bbac08` | `21 02 00 b4` | cbz x1,0x00bbac4c | `CONDITIONAL_JUMP`
<a id="insn-00bbac0c"></a> `00bbac0c` | `75 2b 00 90` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbac10"></a> `00bbac10` | `a8 c2 4e 39` | ldrb w8,[x21, #0x3b0] | `FALL_THROUGH`
<a id="insn-00bbac14"></a> `00bbac14` | `c8 00 00 34` | cbz w8,0x00bbac2c | `CONDITIONAL_JUMP`
<a id="insn-00bbac18"></a> `00bbac18` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbac1c"></a> `00bbac1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbac20"></a> `00bbac20` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bbac24"></a> `00bbac24` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbac28"></a> `00bbac28` | `bf c2 0e 39` | strb wzr,[x21, #0x3b0] | `FALL_THROUGH`
<a id="insn-00bbac2c"></a> `00bbac2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbac30"></a> `00bbac30` | `00 81 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bbac34"></a> `00bbac34` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbac38"></a> `00bbac38` | `81 d6 41 f9` | ldr x1,[x20, #0x3a8] | `FALL_THROUGH`
<a id="insn-00bbac3c"></a> `00bbac3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbac40"></a> `00bbac40` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bbac44"></a> `00bbac44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbac48"></a> `00bbac48` | `9f d6 01 f9` | str xzr,[x20, #0x3a8] | `FALL_THROUGH`
<a id="insn-00bbac4c"></a> `00bbac4c` | `74 2b 00 90` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbac50"></a> `00bbac50` | `81 0e 42 f9` | ldr x1,[x20, #0x418] | `FALL_THROUGH`
<a id="insn-00bbac54"></a> `00bbac54` | `21 02 00 b4` | cbz x1,0x00bbac98 | `CONDITIONAL_JUMP`
<a id="insn-00bbac58"></a> `00bbac58` | `75 2b 00 90` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbac5c"></a> `00bbac5c` | `a8 82 50 39` | ldrb w8,[x21, #0x420] | `FALL_THROUGH`
<a id="insn-00bbac60"></a> `00bbac60` | `c8 00 00 34` | cbz w8,0x00bbac78 | `CONDITIONAL_JUMP`
<a id="insn-00bbac64"></a> `00bbac64` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbac68"></a> `00bbac68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbac6c"></a> `00bbac6c` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bbac70"></a> `00bbac70` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbac74"></a> `00bbac74` | `bf 82 10 39` | strb wzr,[x21, #0x420] | `FALL_THROUGH`
<a id="insn-00bbac78"></a> `00bbac78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbac7c"></a> `00bbac7c` | `ed 80 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bbac80"></a> `00bbac80` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbac84"></a> `00bbac84` | `81 0e 42 f9` | ldr x1,[x20, #0x418] | `FALL_THROUGH`
<a id="insn-00bbac88"></a> `00bbac88` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbac8c"></a> `00bbac8c` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bbac90"></a> `00bbac90` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbac94"></a> `00bbac94` | `9f 0e 02 f9` | str xzr,[x20, #0x418] | `FALL_THROUGH`
<a id="insn-00bbac98"></a> `00bbac98` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbac9c"></a> `00bbac9c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbaca0"></a> `00bbaca0` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bbaca4"></a> `00bbaca4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbabec`](#insn-00bbabec) 範囲 `[['00bbabec', '00bbac0b']]`
  - `CONDITIONAL_JUMP` [`00bbac08`](#insn-00bbac08) → [`00bbac4c`](#insn-00bbac4c)
  - `FALL_THROUGH` [`00bbac08`](#insn-00bbac08) → [`00bbac0c`](#insn-00bbac0c)
- ブロック [`00bbac0c`](#insn-00bbac0c) 範囲 `[['00bbac0c', '00bbac17']]`
  - `CONDITIONAL_JUMP` [`00bbac14`](#insn-00bbac14) → [`00bbac2c`](#insn-00bbac2c)
  - `FALL_THROUGH` [`00bbac14`](#insn-00bbac14) → [`00bbac18`](#insn-00bbac18)
- ブロック [`00bbac18`](#insn-00bbac18) 範囲 `[['00bbac18', '00bbac2b']]`
  - `FALL_THROUGH` [`00bbac28`](#insn-00bbac28) → [`00bbac2c`](#insn-00bbac2c)
- ブロック [`00bbac2c`](#insn-00bbac2c) 範囲 `[['00bbac2c', '00bbac4b']]`
  - `FALL_THROUGH` [`00bbac48`](#insn-00bbac48) → [`00bbac4c`](#insn-00bbac4c)
- ブロック [`00bbac4c`](#insn-00bbac4c) 範囲 `[['00bbac4c', '00bbac57']]`
  - `CONDITIONAL_JUMP` [`00bbac54`](#insn-00bbac54) → [`00bbac98`](#insn-00bbac98)
  - `FALL_THROUGH` [`00bbac54`](#insn-00bbac54) → [`00bbac58`](#insn-00bbac58)
- ブロック [`00bbac58`](#insn-00bbac58) 範囲 `[['00bbac58', '00bbac63']]`
  - `CONDITIONAL_JUMP` [`00bbac60`](#insn-00bbac60) → [`00bbac78`](#insn-00bbac78)
  - `FALL_THROUGH` [`00bbac60`](#insn-00bbac60) → [`00bbac64`](#insn-00bbac64)
- ブロック [`00bbac64`](#insn-00bbac64) 範囲 `[['00bbac64', '00bbac77']]`
  - `FALL_THROUGH` [`00bbac74`](#insn-00bbac74) → [`00bbac78`](#insn-00bbac78)
- ブロック [`00bbac78`](#insn-00bbac78) 範囲 `[['00bbac78', '00bbac97']]`
  - `FALL_THROUGH` [`00bbac94`](#insn-00bbac94) → [`00bbac98`](#insn-00bbac98)
- ブロック [`00bbac98`](#insn-00bbac98) 範囲 `[['00bbac98', '00bbaca7']]`

## 命令位置別の参照

- [`00bbabec`](#insn-00bbabec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbabf0`](#insn-00bbabf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbabf4`](#insn-00bbabf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac00`](#insn-00bbac00) → `011263a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbac08`](#insn-00bbac08) → [`00bbac4c`](#insn-00bbac4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac10`](#insn-00bbac10) → `011263b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbac14`](#insn-00bbac14) → [`00bbac2c`](#insn-00bbac2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac28`](#insn-00bbac28) → `011263b0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbac30`](#insn-00bbac30) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bbac38`](#insn-00bbac38) → `011263a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbac48`](#insn-00bbac48) → `011263a8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbac50`](#insn-00bbac50) → `01126418`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbac54`](#insn-00bbac54) → [`00bbac98`](#insn-00bbac98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac5c`](#insn-00bbac5c) → `01126420`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbac60`](#insn-00bbac60) → [`00bbac78`](#insn-00bbac78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac74`](#insn-00bbac74) → `01126420`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbac7c`](#insn-00bbac7c) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bbac84`](#insn-00bbac84) → `01126418`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbac94`](#insn-00bbac94) → `01126418`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbac98`](#insn-00bbac98) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbac9c`](#insn-00bbac9c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbabec`](#insn-00bbabec)

~~~json
{
  "source": "00bbabec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbabf0`](#insn-00bbabf0)

~~~json
{
  "source": "00bbabf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbabf4`](#insn-00bbabf4)

~~~json
{
  "source": "00bbabf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac00`](#insn-00bbac00)

~~~json
{
  "source": "00bbac00",
  "target": "011263a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011263a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbac08`](#insn-00bbac08)

~~~json
{
  "source": "00bbac08",
  "target": "00bbac4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac10`](#insn-00bbac10)

~~~json
{
  "source": "00bbac10",
  "target": "011263b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011263b0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbac14`](#insn-00bbac14)

~~~json
{
  "source": "00bbac14",
  "target": "00bbac2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac28`](#insn-00bbac28)

~~~json
{
  "source": "00bbac28",
  "target": "011263b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011263b0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbac30`](#insn-00bbac30)

~~~json
{
  "source": "00bbac30",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbac38`](#insn-00bbac38)

~~~json
{
  "source": "00bbac38",
  "target": "011263a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011263a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbac48`](#insn-00bbac48)

~~~json
{
  "source": "00bbac48",
  "target": "011263a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011263a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbac50`](#insn-00bbac50)

~~~json
{
  "source": "00bbac50",
  "target": "01126418",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126418",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbac54`](#insn-00bbac54)

~~~json
{
  "source": "00bbac54",
  "target": "00bbac98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac5c`](#insn-00bbac5c)

~~~json
{
  "source": "00bbac5c",
  "target": "01126420",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126420",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbac60`](#insn-00bbac60)

~~~json
{
  "source": "00bbac60",
  "target": "00bbac78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac74`](#insn-00bbac74)

~~~json
{
  "source": "00bbac74",
  "target": "01126420",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126420",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbac7c`](#insn-00bbac7c)

~~~json
{
  "source": "00bbac7c",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbac84`](#insn-00bbac84)

~~~json
{
  "source": "00bbac84",
  "target": "01126418",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126418",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbac94`](#insn-00bbac94)

~~~json
{
  "source": "00bbac94",
  "target": "01126418",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126418",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbac98`](#insn-00bbac98)

~~~json
{
  "source": "00bbac98",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbac9c`](#insn-00bbac9c)

~~~json
{
  "source": "00bbac9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
