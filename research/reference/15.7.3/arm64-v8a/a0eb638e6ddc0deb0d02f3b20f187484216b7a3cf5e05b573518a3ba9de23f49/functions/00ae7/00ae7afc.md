# 00ae7afc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ae7a34`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7a34.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0059.md#compare-339f31c91210bbf81b6bedb337dd0ee8)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ae7b40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7b40.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0062.md#compare-d065bbd33390ddb26a827527fae1da1a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae7afc",
  "name": "_ZN8firebase4util21asset_file_descriptor12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "72e82865c2e9adff28487d5ef7cc612c465d2807b25e5a8bfbf363e87cd4c787",
  "source_text_sha256": "72e82865c2e9adff28487d5ef7cc612c465d2807b25e5a8bfbf363e87cd4c787",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae7afc",
        "00ae7b9b"
      ]
    ],
    "bytes_sha256": "5a0f69c31168ce35d0cffd0c91a14c8589ba9dfec3341b342b3c36535eb8b3c9",
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

## 疑似コード / UTF-8 716 bytes

~~~c

void _ZN8firebase4util21asset_file_descriptor12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a0560 != 0) {
    if (DAT_010a0568 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a0568 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
                    /* try { // try from 00ae7b6c to 00be7b6f has its CatchHandler @ 00ae8d98 */
                    /* try { // try from 00ae7b70 to 00be7d0b has its CatchHandler @ 00ae6000 */
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a0560);
    DAT_010a0560 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae7afc"></a> `00ae7afc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00ae7b00"></a> `00ae7b00` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae7b04"></a> `00ae7b04` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ae7b08"></a> `00ae7b08` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ae7b0c"></a> `00ae7b0c` | `d4 2d 00 b0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae7b10"></a> `00ae7b10` | `81 b2 42 f9` | ldr x1,[x20, #0x560] | `FALL_THROUGH`
<a id="insn-00ae7b14"></a> `00ae7b14` | `c1 03 00 b4` | cbz x1,0x00ae7b8c | `CONDITIONAL_JUMP`
<a id="insn-00ae7b18"></a> `00ae7b18` | `d5 2d 00 b0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae7b1c"></a> `00ae7b1c` | `a8 a2 55 39` | ldrb w8,[x21, #0x568] | `FALL_THROUGH`
<a id="insn-00ae7b20"></a> `00ae7b20` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ae7b24"></a> `00ae7b24` | `c8 00 00 34` | cbz w8,0x00ae7b3c | `CONDITIONAL_JUMP`
<a id="insn-00ae7b28"></a> `00ae7b28` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae7b2c"></a> `00ae7b2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae7b30"></a> `00ae7b30` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00ae7b34"></a> `00ae7b34` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae7b38"></a> `00ae7b38` | `bf a2 15 39` | strb wzr,[x21, #0x568] | `FALL_THROUGH`
<a id="insn-00ae7b3c"></a> `00ae7b3c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae7b40"></a> `00ae7b40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae7b44"></a> `00ae7b44` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00ae7b48"></a> `00ae7b48` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae7b4c"></a> `00ae7b4c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00ae7b50"></a> `00ae7b50` | `20 01 00 54` | b.eq 0x00ae7b74 | `CONDITIONAL_JUMP`
<a id="insn-00ae7b54"></a> `00ae7b54` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae7b58"></a> `00ae7b58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae7b5c"></a> `00ae7b5c` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00ae7b60"></a> `00ae7b60` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae7b64"></a> `00ae7b64` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae7b68"></a> `00ae7b68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae7b6c"></a> `00ae7b6c` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00ae7b70"></a> `00ae7b70` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae7b74"></a> `00ae7b74` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae7b78"></a> `00ae7b78` | `81 b2 42 f9` | ldr x1,[x20, #0x560] | `FALL_THROUGH`
<a id="insn-00ae7b7c"></a> `00ae7b7c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae7b80"></a> `00ae7b80` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00ae7b84"></a> `00ae7b84` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae7b88"></a> `00ae7b88` | `9f b2 02 f9` | str xzr,[x20, #0x560] | `FALL_THROUGH`
<a id="insn-00ae7b8c"></a> `00ae7b8c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ae7b90"></a> `00ae7b90` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae7b94"></a> `00ae7b94` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00ae7b98"></a> `00ae7b98` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae7afc`](#insn-00ae7afc) 範囲 `[['00ae7afc', '00ae7b17']]`
  - `CONDITIONAL_JUMP` [`00ae7b14`](#insn-00ae7b14) → [`00ae7b8c`](#insn-00ae7b8c)
  - `FALL_THROUGH` [`00ae7b14`](#insn-00ae7b14) → [`00ae7b18`](#insn-00ae7b18)
- ブロック [`00ae7b18`](#insn-00ae7b18) 範囲 `[['00ae7b18', '00ae7b27']]`
  - `CONDITIONAL_JUMP` [`00ae7b24`](#insn-00ae7b24) → [`00ae7b3c`](#insn-00ae7b3c)
  - `FALL_THROUGH` [`00ae7b24`](#insn-00ae7b24) → [`00ae7b28`](#insn-00ae7b28)
- ブロック [`00ae7b28`](#insn-00ae7b28) 範囲 `[['00ae7b28', '00ae7b3b']]`
  - `FALL_THROUGH` [`00ae7b38`](#insn-00ae7b38) → [`00ae7b3c`](#insn-00ae7b3c)
- ブロック [`00ae7b3c`](#insn-00ae7b3c) 範囲 `[['00ae7b3c', '00ae7b53']]`
  - `CONDITIONAL_JUMP` [`00ae7b50`](#insn-00ae7b50) → [`00ae7b74`](#insn-00ae7b74)
  - `FALL_THROUGH` [`00ae7b50`](#insn-00ae7b50) → [`00ae7b54`](#insn-00ae7b54)
- ブロック [`00ae7b54`](#insn-00ae7b54) 範囲 `[['00ae7b54', '00ae7b6b']]`
  - `FALL_THROUGH` [`00ae7b68`](#insn-00ae7b68) → [`00ae7b6c`](#insn-00ae7b6c)
- ブロック [`00ae7b6c`](#insn-00ae7b6c) 範囲 `[['00ae7b6c', '00ae7b6f']]`
  - `FALL_THROUGH` [`00ae7b6c`](#insn-00ae7b6c) → [`00ae7b70`](#insn-00ae7b70)
- ブロック [`00ae7b70`](#insn-00ae7b70) 範囲 `[['00ae7b70', '00ae7b73']]`
  - `FALL_THROUGH` [`00ae7b70`](#insn-00ae7b70) → [`00ae7b74`](#insn-00ae7b74)
- ブロック [`00ae7b74`](#insn-00ae7b74) 範囲 `[['00ae7b74', '00ae7b8b']]`
  - `FALL_THROUGH` [`00ae7b88`](#insn-00ae7b88) → [`00ae7b8c`](#insn-00ae7b8c)
- ブロック [`00ae7b8c`](#insn-00ae7b8c) 範囲 `[['00ae7b8c', '00ae7b9b']]`

## 命令位置別の参照

- [`00ae7afc`](#insn-00ae7afc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7b00`](#insn-00ae7b00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7b04`](#insn-00ae7b04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7b10`](#insn-00ae7b10) → `010a0560`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae7b14`](#insn-00ae7b14) → [`00ae7b8c`](#insn-00ae7b8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7b1c`](#insn-00ae7b1c) → `010a0568`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ae7b24`](#insn-00ae7b24) → [`00ae7b3c`](#insn-00ae7b3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7b38`](#insn-00ae7b38) → `010a0568`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ae7b50`](#insn-00ae7b50) → [`00ae7b74`](#insn-00ae7b74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7b78`](#insn-00ae7b78) → `010a0560`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae7b88`](#insn-00ae7b88) → `010a0560`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae7b8c`](#insn-00ae7b8c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7b90`](#insn-00ae7b90) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae7afc`](#insn-00ae7afc)

~~~json
{
  "source": "00ae7afc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7b00`](#insn-00ae7b00)

~~~json
{
  "source": "00ae7b00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7b04`](#insn-00ae7b04)

~~~json
{
  "source": "00ae7b04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7b10`](#insn-00ae7b10)

~~~json
{
  "source": "00ae7b10",
  "target": "010a0560",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0560",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae7b14`](#insn-00ae7b14)

~~~json
{
  "source": "00ae7b14",
  "target": "00ae7b8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7b1c`](#insn-00ae7b1c)

~~~json
{
  "source": "00ae7b1c",
  "target": "010a0568",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0568",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae7b24`](#insn-00ae7b24)

~~~json
{
  "source": "00ae7b24",
  "target": "00ae7b3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7b38`](#insn-00ae7b38)

~~~json
{
  "source": "00ae7b38",
  "target": "010a0568",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0568",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae7b50`](#insn-00ae7b50)

~~~json
{
  "source": "00ae7b50",
  "target": "00ae7b74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7b78`](#insn-00ae7b78)

~~~json
{
  "source": "00ae7b78",
  "target": "010a0560",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0560",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae7b88`](#insn-00ae7b88)

~~~json
{
  "source": "00ae7b88",
  "target": "010a0560",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0560",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae7b8c`](#insn-00ae7b8c)

~~~json
{
  "source": "00ae7b8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7b90`](#insn-00ae7b90)

~~~json
{
  "source": "00ae7b90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
