//> using scala "2.13"

import java.io.File
import scala.io.Source

// First take only one row containing a given image URL
// (some figure images seem to duplicated across treatment entries)
// then group by family and retain up to 3 figures
val allLines = Source.fromFile(new File(args(0)), "UTF-8")
    .getLines()
    .drop(1)
    .map(_.split("\t", -1))
    .toSeq
    .groupBy(items => items(4))
    .flatMap { case (url, rows) =>
        rows.take(1)
    }
    .groupBy(items => items(0))
    .view
    .view
    .mapValues(_.toSeq.sortBy(items => items.mkString).take(3))
    .foreach {case (family, rows) => 
        rows.foreach { items =>
            println(items.mkString("\t"))
        }
    }
