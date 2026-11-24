# 00bd1bfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bd17d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd17d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0082.md#compare-f4745c4f0f2ed7b3bc0267adffa12444)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd1c98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd1/00bd1c98.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0082.md#compare-596f8517addb000242afa5c77ac9ce47)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd1bfc",
  "name": "_ZN8firebase4auth29invalid_credentials_exception12ReleaseClassEP7_JNIEnv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "035f545430ee8ff98fb7cdda227200cdcc28542a1cc30d1a08c872bef094feba",
  "source_text_sha256": "035f545430ee8ff98fb7cdda227200cdcc28542a1cc30d1a08c872bef094feba",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd1bfc",
        "00bd1c6b"
      ]
    ],
    "bytes_sha256": "098d957f2b11864c2bea7330de87c032e48c63c5105b98658cbe4234a81a637a",
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

- [00c5af60](../00c5a/00c5af60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 404 bytes

~~~c

void _ZN8firebase4auth29invalid_credentials_exception12ReleaseClassEP7_JNIEnv(long *param_1)

{
  if (DAT_01126928 != 0) {
    if (DAT_01126930 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126930 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126928);
    DAT_01126928 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd1bfc"></a> `00bd1bfc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bd1c00"></a> `00bd1c00` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1c04"></a> `00bd1c04` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd1c08"></a> `00bd1c08` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bd1c0c"></a> `00bd1c0c` | `b4 2a 00 b0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd1c10"></a> `00bd1c10` | `81 96 44 f9` | ldr x1,[x20, #0x928] | `FALL_THROUGH`
<a id="insn-00bd1c14"></a> `00bd1c14` | `41 02 00 b4` | cbz x1,0x00bd1c5c | `CONDITIONAL_JUMP`
<a id="insn-00bd1c18"></a> `00bd1c18` | `b5 2a 00 b0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd1c1c"></a> `00bd1c1c` | `a8 c2 64 39` | ldrb w8,[x21, #0x930] | `FALL_THROUGH`
<a id="insn-00bd1c20"></a> `00bd1c20` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bd1c24"></a> `00bd1c24` | `c8 00 00 34` | cbz w8,0x00bd1c3c | `CONDITIONAL_JUMP`
<a id="insn-00bd1c28"></a> `00bd1c28` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd1c2c"></a> `00bd1c2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd1c30"></a> `00bd1c30` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bd1c34"></a> `00bd1c34` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd1c38"></a> `00bd1c38` | `bf c2 24 39` | strb wzr,[x21, #0x930] | `FALL_THROUGH`
<a id="insn-00bd1c3c"></a> `00bd1c3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd1c40"></a> `00bd1c40` | `c8 24 02 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bd1c44"></a> `00bd1c44` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd1c48"></a> `00bd1c48` | `81 96 44 f9` | ldr x1,[x20, #0x928] | `FALL_THROUGH`
<a id="insn-00bd1c4c"></a> `00bd1c4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd1c50"></a> `00bd1c50` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd1c54"></a> `00bd1c54` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd1c58"></a> `00bd1c58` | `9f 96 04 f9` | str xzr,[x20, #0x928] | `FALL_THROUGH`
<a id="insn-00bd1c5c"></a> `00bd1c5c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd1c60"></a> `00bd1c60` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1c64"></a> `00bd1c64` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd1c68"></a> `00bd1c68` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd1bfc`](#insn-00bd1bfc) 範囲 `[['00bd1bfc', '00bd1c17']]`
  - `CONDITIONAL_JUMP` [`00bd1c14`](#insn-00bd1c14) → [`00bd1c5c`](#insn-00bd1c5c)
  - `FALL_THROUGH` [`00bd1c14`](#insn-00bd1c14) → [`00bd1c18`](#insn-00bd1c18)
- ブロック [`00bd1c18`](#insn-00bd1c18) 範囲 `[['00bd1c18', '00bd1c27']]`
  - `CONDITIONAL_JUMP` [`00bd1c24`](#insn-00bd1c24) → [`00bd1c3c`](#insn-00bd1c3c)
  - `FALL_THROUGH` [`00bd1c24`](#insn-00bd1c24) → [`00bd1c28`](#insn-00bd1c28)
- ブロック [`00bd1c28`](#insn-00bd1c28) 範囲 `[['00bd1c28', '00bd1c3b']]`
  - `FALL_THROUGH` [`00bd1c38`](#insn-00bd1c38) → [`00bd1c3c`](#insn-00bd1c3c)
- ブロック [`00bd1c3c`](#insn-00bd1c3c) 範囲 `[['00bd1c3c', '00bd1c5b']]`
  - `FALL_THROUGH` [`00bd1c58`](#insn-00bd1c58) → [`00bd1c5c`](#insn-00bd1c5c)
- ブロック [`00bd1c5c`](#insn-00bd1c5c) 範囲 `[['00bd1c5c', '00bd1c6b']]`

## 命令位置別の参照

- [`00bd1bfc`](#insn-00bd1bfc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1c00`](#insn-00bd1c00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1c04`](#insn-00bd1c04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1c10`](#insn-00bd1c10) → `01126928`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd1c14`](#insn-00bd1c14) → [`00bd1c5c`](#insn-00bd1c5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1c1c`](#insn-00bd1c1c) → `01126930`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd1c24`](#insn-00bd1c24) → [`00bd1c3c`](#insn-00bd1c3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1c38`](#insn-00bd1c38) → `01126930`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd1c40`](#insn-00bd1c40) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bd1c48`](#insn-00bd1c48) → `01126928`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd1c58`](#insn-00bd1c58) → `01126928`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd1c5c`](#insn-00bd1c5c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1c60`](#insn-00bd1c60) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd1bfc`](#insn-00bd1bfc)

~~~json
{
  "source": "00bd1bfc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1c00`](#insn-00bd1c00)

~~~json
{
  "source": "00bd1c00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1c04`](#insn-00bd1c04)

~~~json
{
  "source": "00bd1c04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1c10`](#insn-00bd1c10)

~~~json
{
  "source": "00bd1c10",
  "target": "01126928",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126928",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd1c14`](#insn-00bd1c14)

~~~json
{
  "source": "00bd1c14",
  "target": "00bd1c5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1c1c`](#insn-00bd1c1c)

~~~json
{
  "source": "00bd1c1c",
  "target": "01126930",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126930",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd1c24`](#insn-00bd1c24)

~~~json
{
  "source": "00bd1c24",
  "target": "00bd1c3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1c38`](#insn-00bd1c38)

~~~json
{
  "source": "00bd1c38",
  "target": "01126930",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126930",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd1c40`](#insn-00bd1c40)

~~~json
{
  "source": "00bd1c40",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd1c48`](#insn-00bd1c48)

~~~json
{
  "source": "00bd1c48",
  "target": "01126928",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126928",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd1c58`](#insn-00bd1c58)

~~~json
{
  "source": "00bd1c58",
  "target": "01126928",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126928",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd1c5c`](#insn-00bd1c5c)

~~~json
{
  "source": "00bd1c5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1c60`](#insn-00bd1c60)

~~~json
{
  "source": "00bd1c60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
