# 00b4ddec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b4cdf8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cdf8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0075.md#compare-1121d6dfa1c22bd1b47be7b1d076f1e7)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4ddec",
  "name": "_ZN8firebase4util22parcel_file_descriptor12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9c7da6c31876c9fbd0abdf50670e05d17a9ec9cecb550dedfd46ff54a083063e",
  "source_text_sha256": "9c7da6c31876c9fbd0abdf50670e05d17a9ec9cecb550dedfd46ff54a083063e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4ddec",
        "00b4de8b"
      ]
    ],
    "bytes_sha256": "28f0ee943936d8c87865866690d2dd6c77dc9946acaa212e142b9db40566c811",
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

## 疑似コード / UTF-8 523 bytes

~~~c

void _ZN8firebase4util22parcel_file_descriptor12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_01126d28 != 0) {
    if (DAT_01126d30 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126d30 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126d28);
    DAT_01126d28 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4ddec"></a> `00b4ddec` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b4ddf0"></a> `00b4ddf0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4ddf4"></a> `00b4ddf4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4ddf8"></a> `00b4ddf8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b4ddfc"></a> `00b4ddfc` | `d4 2e 00 b0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00b4de00"></a> `00b4de00` | `81 96 46 f9` | ldr x1,[x20, #0xd28] | `FALL_THROUGH`
<a id="insn-00b4de04"></a> `00b4de04` | `c1 03 00 b4` | cbz x1,0x00b4de7c | `CONDITIONAL_JUMP`
<a id="insn-00b4de08"></a> `00b4de08` | `d5 2e 00 b0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00b4de0c"></a> `00b4de0c` | `a8 c2 74 39` | ldrb w8,[x21, #0xd30] | `FALL_THROUGH`
<a id="insn-00b4de10"></a> `00b4de10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b4de14"></a> `00b4de14` | `c8 00 00 34` | cbz w8,0x00b4de2c | `CONDITIONAL_JUMP`
<a id="insn-00b4de18"></a> `00b4de18` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4de1c"></a> `00b4de1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4de20"></a> `00b4de20` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00b4de24"></a> `00b4de24` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4de28"></a> `00b4de28` | `bf c2 34 39` | strb wzr,[x21, #0xd30] | `FALL_THROUGH`
<a id="insn-00b4de2c"></a> `00b4de2c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4de30"></a> `00b4de30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4de34"></a> `00b4de34` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00b4de38"></a> `00b4de38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4de3c"></a> `00b4de3c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00b4de40"></a> `00b4de40` | `20 01 00 54` | b.eq 0x00b4de64 | `CONDITIONAL_JUMP`
<a id="insn-00b4de44"></a> `00b4de44` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4de48"></a> `00b4de48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4de4c"></a> `00b4de4c` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00b4de50"></a> `00b4de50` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4de54"></a> `00b4de54` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4de58"></a> `00b4de58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4de5c"></a> `00b4de5c` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00b4de60"></a> `00b4de60` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4de64"></a> `00b4de64` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4de68"></a> `00b4de68` | `81 96 46 f9` | ldr x1,[x20, #0xd28] | `FALL_THROUGH`
<a id="insn-00b4de6c"></a> `00b4de6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4de70"></a> `00b4de70` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00b4de74"></a> `00b4de74` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4de78"></a> `00b4de78` | `9f 96 06 f9` | str xzr,[x20, #0xd28] | `FALL_THROUGH`
<a id="insn-00b4de7c"></a> `00b4de7c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4de80"></a> `00b4de80` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4de84"></a> `00b4de84` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b4de88"></a> `00b4de88` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4ddec`](#insn-00b4ddec) 範囲 `[['00b4ddec', '00b4de07']]`
  - `CONDITIONAL_JUMP` [`00b4de04`](#insn-00b4de04) → [`00b4de7c`](#insn-00b4de7c)
  - `FALL_THROUGH` [`00b4de04`](#insn-00b4de04) → [`00b4de08`](#insn-00b4de08)
- ブロック [`00b4de08`](#insn-00b4de08) 範囲 `[['00b4de08', '00b4de17']]`
  - `CONDITIONAL_JUMP` [`00b4de14`](#insn-00b4de14) → [`00b4de2c`](#insn-00b4de2c)
  - `FALL_THROUGH` [`00b4de14`](#insn-00b4de14) → [`00b4de18`](#insn-00b4de18)
- ブロック [`00b4de18`](#insn-00b4de18) 範囲 `[['00b4de18', '00b4de2b']]`
  - `FALL_THROUGH` [`00b4de28`](#insn-00b4de28) → [`00b4de2c`](#insn-00b4de2c)
- ブロック [`00b4de2c`](#insn-00b4de2c) 範囲 `[['00b4de2c', '00b4de43']]`
  - `CONDITIONAL_JUMP` [`00b4de40`](#insn-00b4de40) → [`00b4de64`](#insn-00b4de64)
  - `FALL_THROUGH` [`00b4de40`](#insn-00b4de40) → [`00b4de44`](#insn-00b4de44)
- ブロック [`00b4de44`](#insn-00b4de44) 範囲 `[['00b4de44', '00b4de63']]`
  - `FALL_THROUGH` [`00b4de60`](#insn-00b4de60) → [`00b4de64`](#insn-00b4de64)
- ブロック [`00b4de64`](#insn-00b4de64) 範囲 `[['00b4de64', '00b4de7b']]`
  - `FALL_THROUGH` [`00b4de78`](#insn-00b4de78) → [`00b4de7c`](#insn-00b4de7c)
- ブロック [`00b4de7c`](#insn-00b4de7c) 範囲 `[['00b4de7c', '00b4de8b']]`

## 命令位置別の参照

- [`00b4ddec`](#insn-00b4ddec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ddf0`](#insn-00b4ddf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ddf4`](#insn-00b4ddf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4de00`](#insn-00b4de00) → `01126d28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4de04`](#insn-00b4de04) → [`00b4de7c`](#insn-00b4de7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4de0c`](#insn-00b4de0c) → `01126d30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4de14`](#insn-00b4de14) → [`00b4de2c`](#insn-00b4de2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4de28`](#insn-00b4de28) → `01126d30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4de40`](#insn-00b4de40) → [`00b4de64`](#insn-00b4de64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4de68`](#insn-00b4de68) → `01126d28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4de78`](#insn-00b4de78) → `01126d28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4de7c`](#insn-00b4de7c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4de80`](#insn-00b4de80) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4ddec`](#insn-00b4ddec)

~~~json
{
  "source": "00b4ddec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ddf0`](#insn-00b4ddf0)

~~~json
{
  "source": "00b4ddf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ddf4`](#insn-00b4ddf4)

~~~json
{
  "source": "00b4ddf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4de00`](#insn-00b4de00)

~~~json
{
  "source": "00b4de00",
  "target": "01126d28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4de04`](#insn-00b4de04)

~~~json
{
  "source": "00b4de04",
  "target": "00b4de7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4de0c`](#insn-00b4de0c)

~~~json
{
  "source": "00b4de0c",
  "target": "01126d30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d30",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4de14`](#insn-00b4de14)

~~~json
{
  "source": "00b4de14",
  "target": "00b4de2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4de28`](#insn-00b4de28)

~~~json
{
  "source": "00b4de28",
  "target": "01126d30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d30",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4de40`](#insn-00b4de40)

~~~json
{
  "source": "00b4de40",
  "target": "00b4de64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4de68`](#insn-00b4de68)

~~~json
{
  "source": "00b4de68",
  "target": "01126d28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4de78`](#insn-00b4de78)

~~~json
{
  "source": "00b4de78",
  "target": "01126d28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4de7c`](#insn-00b4de7c)

~~~json
{
  "source": "00b4de7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4de80`](#insn-00b4de80)

~~~json
{
  "source": "00b4de80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
