# 00aeddf8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aeddb4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aeddb4.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-a2a9ae4a2a45255a1c46828822685ccc)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4db7c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4db7c.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0059.md#compare-db3e378bf12803b9c9f6bc03f2c93077)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeddf8",
  "name": "_ZN8firebase4util3uri12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ed34ff4736e415cbdb390da2539337b84b9920fd5d1fb3fa2daee090e22a58cc",
  "source_text_sha256": "ed34ff4736e415cbdb390da2539337b84b9920fd5d1fb3fa2daee090e22a58cc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeddf8",
        "00aede97"
      ]
    ],
    "bytes_sha256": "e3c997f32744524164174392084e8df41840e3d43118677ff01aa00a54d2797f",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 5,
    "unresolved": 5
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 503 bytes

~~~c

void _ZN8firebase4util3uri12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a0a60 != 0) {
    if (DAT_010a0a68 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a0a68 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a0a60);
    DAT_010a0a60 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeddf8"></a> `00aeddf8` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aeddfc"></a> `00aeddfc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aede00"></a> `00aede00` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aede04"></a> `00aede04` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aede08"></a> `00aede08` | `94 2d 00 f0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aede0c"></a> `00aede0c` | `81 32 45 f9` | ldr x1,[x20, #0xa60] | `FALL_THROUGH`
<a id="insn-00aede10"></a> `00aede10` | `c1 03 00 b4` | cbz x1,0x00aede88 | `CONDITIONAL_JUMP`
<a id="insn-00aede14"></a> `00aede14` | `95 2d 00 f0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aede18"></a> `00aede18` | `a8 a2 69 39` | ldrb w8,[x21, #0xa68] | `FALL_THROUGH`
<a id="insn-00aede1c"></a> `00aede1c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aede20"></a> `00aede20` | `c8 00 00 34` | cbz w8,0x00aede38 | `CONDITIONAL_JUMP`
<a id="insn-00aede24"></a> `00aede24` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aede28"></a> `00aede28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aede2c"></a> `00aede2c` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00aede30"></a> `00aede30` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aede34"></a> `00aede34` | `bf a2 29 39` | strb wzr,[x21, #0xa68] | `FALL_THROUGH`
<a id="insn-00aede38"></a> `00aede38` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aede3c"></a> `00aede3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aede40"></a> `00aede40` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aede44"></a> `00aede44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aede48"></a> `00aede48` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aede4c"></a> `00aede4c` | `20 01 00 54` | b.eq 0x00aede70 | `CONDITIONAL_JUMP`
<a id="insn-00aede50"></a> `00aede50` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aede54"></a> `00aede54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aede58"></a> `00aede58` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aede5c"></a> `00aede5c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aede60"></a> `00aede60` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aede64"></a> `00aede64` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aede68"></a> `00aede68` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aede6c"></a> `00aede6c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aede70"></a> `00aede70` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aede74"></a> `00aede74` | `81 32 45 f9` | ldr x1,[x20, #0xa60] | `FALL_THROUGH`
<a id="insn-00aede78"></a> `00aede78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aede7c"></a> `00aede7c` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00aede80"></a> `00aede80` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aede84"></a> `00aede84` | `9f 32 05 f9` | str xzr,[x20, #0xa60] | `FALL_THROUGH`
<a id="insn-00aede88"></a> `00aede88` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aede8c"></a> `00aede8c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aede90"></a> `00aede90` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aede94"></a> `00aede94` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeddf8`](#insn-00aeddf8) 範囲 `[['00aeddf8', '00aede13']]`
  - `CONDITIONAL_JUMP` [`00aede10`](#insn-00aede10) → [`00aede88`](#insn-00aede88)
  - `FALL_THROUGH` [`00aede10`](#insn-00aede10) → [`00aede14`](#insn-00aede14)
- ブロック [`00aede14`](#insn-00aede14) 範囲 `[['00aede14', '00aede23']]`
  - `CONDITIONAL_JUMP` [`00aede20`](#insn-00aede20) → [`00aede38`](#insn-00aede38)
  - `FALL_THROUGH` [`00aede20`](#insn-00aede20) → [`00aede24`](#insn-00aede24)
- ブロック [`00aede24`](#insn-00aede24) 範囲 `[['00aede24', '00aede37']]`
  - `FALL_THROUGH` [`00aede34`](#insn-00aede34) → [`00aede38`](#insn-00aede38)
- ブロック [`00aede38`](#insn-00aede38) 範囲 `[['00aede38', '00aede4f']]`
  - `CONDITIONAL_JUMP` [`00aede4c`](#insn-00aede4c) → [`00aede70`](#insn-00aede70)
  - `FALL_THROUGH` [`00aede4c`](#insn-00aede4c) → [`00aede50`](#insn-00aede50)
- ブロック [`00aede50`](#insn-00aede50) 範囲 `[['00aede50', '00aede6f']]`
  - `FALL_THROUGH` [`00aede6c`](#insn-00aede6c) → [`00aede70`](#insn-00aede70)
- ブロック [`00aede70`](#insn-00aede70) 範囲 `[['00aede70', '00aede87']]`
  - `FALL_THROUGH` [`00aede84`](#insn-00aede84) → [`00aede88`](#insn-00aede88)
- ブロック [`00aede88`](#insn-00aede88) 範囲 `[['00aede88', '00aede97']]`

## 命令位置別の参照

- [`00aeddf8`](#insn-00aeddf8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeddfc`](#insn-00aeddfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aede00`](#insn-00aede00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aede0c`](#insn-00aede0c) → `010a0a60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aede10`](#insn-00aede10) → [`00aede88`](#insn-00aede88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aede18`](#insn-00aede18) → `010a0a68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aede20`](#insn-00aede20) → [`00aede38`](#insn-00aede38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aede34`](#insn-00aede34) → `010a0a68`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aede4c`](#insn-00aede4c) → [`00aede70`](#insn-00aede70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aede74`](#insn-00aede74) → `010a0a60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aede84`](#insn-00aede84) → `010a0a60`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aede88`](#insn-00aede88) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aede8c`](#insn-00aede8c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeddf8`](#insn-00aeddf8)

~~~json
{
  "source": "00aeddf8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeddfc`](#insn-00aeddfc)

~~~json
{
  "source": "00aeddfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aede00`](#insn-00aede00)

~~~json
{
  "source": "00aede00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aede0c`](#insn-00aede0c)

~~~json
{
  "source": "00aede0c",
  "target": "010a0a60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aede10`](#insn-00aede10)

~~~json
{
  "source": "00aede10",
  "target": "00aede88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aede18`](#insn-00aede18)

~~~json
{
  "source": "00aede18",
  "target": "010a0a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a68",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aede20`](#insn-00aede20)

~~~json
{
  "source": "00aede20",
  "target": "00aede38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aede34`](#insn-00aede34)

~~~json
{
  "source": "00aede34",
  "target": "010a0a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a68",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aede4c`](#insn-00aede4c)

~~~json
{
  "source": "00aede4c",
  "target": "00aede70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aede74`](#insn-00aede74)

~~~json
{
  "source": "00aede74",
  "target": "010a0a60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aede84`](#insn-00aede84)

~~~json
{
  "source": "00aede84",
  "target": "010a0a60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aede88`](#insn-00aede88)

~~~json
{
  "source": "00aede88",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aede8c`](#insn-00aede8c)

~~~json
{
  "source": "00aede8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
