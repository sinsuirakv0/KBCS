# 00aedcec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aeddb4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aeddb4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-bfa90bc350ec7058078b725f4be187cb)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aedcec",
  "name": "_ZN8firebase4util3uri12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1e02cc55d42c6fca49b1ed4b92ced25df40cb13d2f0f926736c98d4c7ceb96e6",
  "source_text_sha256": "1e02cc55d42c6fca49b1ed4b92ced25df40cb13d2f0f926736c98d4c7ceb96e6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aedcec",
        "00aedd8b"
      ]
    ],
    "bytes_sha256": "567d35af4f1cbc98e74f53655ae669f56636672f0ae64d70feaea4c5cf181959",
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
  
  if (DAT_010a0960 != 0) {
    if (DAT_010a0968 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a0968 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a0960);
    DAT_010a0960 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aedcec"></a> `00aedcec` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aedcf0"></a> `00aedcf0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedcf4"></a> `00aedcf4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aedcf8"></a> `00aedcf8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aedcfc"></a> `00aedcfc` | `94 2d 00 f0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedd00"></a> `00aedd00` | `81 b2 44 f9` | ldr x1,[x20, #0x960] | `FALL_THROUGH`
<a id="insn-00aedd04"></a> `00aedd04` | `c1 03 00 b4` | cbz x1,0x00aedd7c | `CONDITIONAL_JUMP`
<a id="insn-00aedd08"></a> `00aedd08` | `95 2d 00 f0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedd0c"></a> `00aedd0c` | `a8 a2 65 39` | ldrb w8,[x21, #0x968] | `FALL_THROUGH`
<a id="insn-00aedd10"></a> `00aedd10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aedd14"></a> `00aedd14` | `c8 00 00 34` | cbz w8,0x00aedd2c | `CONDITIONAL_JUMP`
<a id="insn-00aedd18"></a> `00aedd18` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aedd1c"></a> `00aedd1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aedd20"></a> `00aedd20` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00aedd24"></a> `00aedd24` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aedd28"></a> `00aedd28` | `bf a2 25 39` | strb wzr,[x21, #0x968] | `FALL_THROUGH`
<a id="insn-00aedd2c"></a> `00aedd2c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aedd30"></a> `00aedd30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aedd34"></a> `00aedd34` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aedd38"></a> `00aedd38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aedd3c"></a> `00aedd3c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aedd40"></a> `00aedd40` | `20 01 00 54` | b.eq 0x00aedd64 | `CONDITIONAL_JUMP`
<a id="insn-00aedd44"></a> `00aedd44` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aedd48"></a> `00aedd48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aedd4c"></a> `00aedd4c` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aedd50"></a> `00aedd50` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aedd54"></a> `00aedd54` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aedd58"></a> `00aedd58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aedd5c"></a> `00aedd5c` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aedd60"></a> `00aedd60` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aedd64"></a> `00aedd64` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aedd68"></a> `00aedd68` | `81 b2 44 f9` | ldr x1,[x20, #0x960] | `FALL_THROUGH`
<a id="insn-00aedd6c"></a> `00aedd6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aedd70"></a> `00aedd70` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00aedd74"></a> `00aedd74` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aedd78"></a> `00aedd78` | `9f b2 04 f9` | str xzr,[x20, #0x960] | `FALL_THROUGH`
<a id="insn-00aedd7c"></a> `00aedd7c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aedd80"></a> `00aedd80` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedd84"></a> `00aedd84` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aedd88"></a> `00aedd88` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aedcec`](#insn-00aedcec) 範囲 `[['00aedcec', '00aedd07']]`
  - `CONDITIONAL_JUMP` [`00aedd04`](#insn-00aedd04) → [`00aedd7c`](#insn-00aedd7c)
  - `FALL_THROUGH` [`00aedd04`](#insn-00aedd04) → [`00aedd08`](#insn-00aedd08)
- ブロック [`00aedd08`](#insn-00aedd08) 範囲 `[['00aedd08', '00aedd17']]`
  - `CONDITIONAL_JUMP` [`00aedd14`](#insn-00aedd14) → [`00aedd2c`](#insn-00aedd2c)
  - `FALL_THROUGH` [`00aedd14`](#insn-00aedd14) → [`00aedd18`](#insn-00aedd18)
- ブロック [`00aedd18`](#insn-00aedd18) 範囲 `[['00aedd18', '00aedd2b']]`
  - `FALL_THROUGH` [`00aedd28`](#insn-00aedd28) → [`00aedd2c`](#insn-00aedd2c)
- ブロック [`00aedd2c`](#insn-00aedd2c) 範囲 `[['00aedd2c', '00aedd43']]`
  - `CONDITIONAL_JUMP` [`00aedd40`](#insn-00aedd40) → [`00aedd64`](#insn-00aedd64)
  - `FALL_THROUGH` [`00aedd40`](#insn-00aedd40) → [`00aedd44`](#insn-00aedd44)
- ブロック [`00aedd44`](#insn-00aedd44) 範囲 `[['00aedd44', '00aedd63']]`
  - `FALL_THROUGH` [`00aedd60`](#insn-00aedd60) → [`00aedd64`](#insn-00aedd64)
- ブロック [`00aedd64`](#insn-00aedd64) 範囲 `[['00aedd64', '00aedd7b']]`
  - `FALL_THROUGH` [`00aedd78`](#insn-00aedd78) → [`00aedd7c`](#insn-00aedd7c)
- ブロック [`00aedd7c`](#insn-00aedd7c) 範囲 `[['00aedd7c', '00aedd8b']]`

## 命令位置別の参照

- [`00aedcec`](#insn-00aedcec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedcf0`](#insn-00aedcf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedcf4`](#insn-00aedcf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedd00`](#insn-00aedd00) → `010a0960`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedd04`](#insn-00aedd04) → [`00aedd7c`](#insn-00aedd7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedd0c`](#insn-00aedd0c) → `010a0968`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aedd14`](#insn-00aedd14) → [`00aedd2c`](#insn-00aedd2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedd28`](#insn-00aedd28) → `010a0968`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aedd40`](#insn-00aedd40) → [`00aedd64`](#insn-00aedd64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedd68`](#insn-00aedd68) → `010a0960`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedd78`](#insn-00aedd78) → `010a0960`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedd7c`](#insn-00aedd7c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedd80`](#insn-00aedd80) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aedcec`](#insn-00aedcec)

~~~json
{
  "source": "00aedcec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedcf0`](#insn-00aedcf0)

~~~json
{
  "source": "00aedcf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedcf4`](#insn-00aedcf4)

~~~json
{
  "source": "00aedcf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedd00`](#insn-00aedd00)

~~~json
{
  "source": "00aedd00",
  "target": "010a0960",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0960",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedd04`](#insn-00aedd04)

~~~json
{
  "source": "00aedd04",
  "target": "00aedd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedd0c`](#insn-00aedd0c)

~~~json
{
  "source": "00aedd0c",
  "target": "010a0968",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0968",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedd14`](#insn-00aedd14)

~~~json
{
  "source": "00aedd14",
  "target": "00aedd2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedd28`](#insn-00aedd28)

~~~json
{
  "source": "00aedd28",
  "target": "010a0968",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0968",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedd40`](#insn-00aedd40)

~~~json
{
  "source": "00aedd40",
  "target": "00aedd64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedd68`](#insn-00aedd68)

~~~json
{
  "source": "00aedd68",
  "target": "010a0960",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0960",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedd78`](#insn-00aedd78)

~~~json
{
  "source": "00aedd78",
  "target": "010a0960",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0960",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedd7c`](#insn-00aedd7c)

~~~json
{
  "source": "00aedd7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedd80`](#insn-00aedd80)

~~~json
{
  "source": "00aedd80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
